from zope.interface import implements
from zope.schema.vocabulary import getVocabularyRegistry
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import ISource


class WrappedVocabulary(object):
    def __init__(self, vocab, hidden_terms):
        self.vocab, self.hidden_terms = vocab, hidden_terms
    def __contains__(self, name):
        return getattr(self.vocab, '__contains__')(name)
    def __getattr__(self, name):
        return getattr(self.vocab, name)
    def __len__(self):
        return len(self.vocab)
    def search(self, *args, **kw):
        for term in self.vocab.search(*args, **kw):
            if term.value not in self.hidden_terms:
                yield term
    def __iter__(self):
        for term in self.vocab:
            if term.value not in self.hidden_terms:
                yield term

def wrap_vocabulary(original_vocab, hidden_terms=[],
                    wrap_with=WrappedVocabulary):
    return HiddenTermsVocabulary(original_vocab, hidden_terms, wrap_with)

class HiddenTermsVocabulary(object):

    implements(IVocabularyFactory, ISource)

    def __init__(self, original_vocab, hidden_terms=[],
                 wrap_with=WrappedVocabulary):
        self.original_vocab = original_vocab
        self.hidden_terms = hidden_terms
        self.wrap_with = wrap_with

    def __call__(self, context):
        if isinstance(self.original_vocab, basestring):
            original_vocab = getVocabularyRegistry().get(
                    context, self.original_vocab)
        else:
            original_vocab = self.original_vocab

        if callable(self.hidden_terms):
            self.hidden_terms = self.hidden_terms(contex, original_vocab)

        if not getattr(original_vocab, 'hidden_terms', None) and \
           isinstance(original_vocab, list):
            self.hidden_terms += original_vocab.hidden_terms

        return self.wrap_with(original_vocab, self.hidden_terms)


