from zope.interface import implements
from zope.schema.vocabulary import getVocabularyRegistry
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import IContextSourceBinder


class VocabularyFactory(object):

    implements(IVocabularyFactory, IContextSourceBinder)

    def __init__(self, original_vocab, hidden_terms, wrapper):
        self.original_vocab = original_vocab
        self.hidden_terms = hidden_terms
        self.wrapper = wrapper

    def __call__(self, context):
        if isinstance(self.original_vocab, basestring):
            original_vocab = getVocabularyRegistry().get(
                    context, self.original_vocab)
        else:
            original_vocab = self.original_vocab

        if callable(self.hidden_terms):
            self.hidden_terms = self.hidden_terms(context, original_vocab)

        if getattr(original_vocab, 'hidden_terms', False) and \
           isinstance(original_vocab.hidden_terms, list):
            self.hidden_terms += original_vocab.hidden_terms

        return self.wrapper(original_vocab, self.hidden_terms)
