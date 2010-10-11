from zope.interface import implements
from zope.schema.vocabulary import getVocabularyRegistry
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IContextSourceBinder

from collective.elephantvocabulary.base import WrapperBase


class VocabularyFactory(object):

    implements(IVocabularyFactory, IContextSourceBinder)

    def __init__(self, vocab, visible_terms=None, hidden_terms=None,
                 wrapper_class=WrapperBase):
        self.vocab = vocab
        self.visible_terms = visible_terms
        self.hidden_terms = hidden_terms
        self.wrapper_class = wrapper_class

    def __call__(self, context):
        if isinstance(self.vocab, basestring):
            original_vocab = getVocabularyRegistry().get(
                    context, self.vocab)
        else:
            original_vocab = self.vocab

        if callable(self.visible_terms):
            self.visible_terms = self.visible_terms(context, original_vocab)

        if getattr(original_vocab, 'visible_terms', False) and \
           isinstance(original_vocab.visible_terms, list):
            if self.visible_terms is None:
                self.visible_terms = original_vocab.visible_terms
            else:
                self.visible_terms += original_vocab.visible_terms

        if callable(self.hidden_terms):
            self.hidden_terms = self.hidden_terms(context, original_vocab)

        if getattr(original_vocab, 'hidden_terms', False) and \
           isinstance(original_vocab.hidden_terms, list):
            if self.hidden_terms is None:
                self.hidden_terms = original_vocab.hidden_terms
            else:
                self.hidden_terms += original_vocab.hidden_terms

        return self.wrapper_class(original_vocab,
                    visible_terms=self.visible_terms,
                    hidden_terms=self.hidden_terms)
