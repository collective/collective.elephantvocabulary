from zope.schema.vocabulary import getVocabularyRegistry


class WrappedVocabulary(object):
    def __init__(self, vocab, hidden_terms):
        self.vocab, self.hidden_terms = vocab, hidden_terms
    def __contains__(self, name):
        return getattr(self.vocab, '__contains__')(name)
    def __getattr__(self, name):
        return getattr(self.vocab, name)
    def __len__(self):
        return getattr(self.vocab, '__len__')()
    def __iter__(self):
        for term in self.vocab:
            if term.value not in self.hidden_terms:
                yield term


class HiddenTermsVocabulary(object):

    def __init__(self, original_vocab, hidden_terms=[],
                 wrap_with=WrappedVocabulary):
        self.original_vocab = original_vocab
        self.hidden_terms = hidden_terms
        self.wrap_with = wrap_with

    def __call__(self, context):
        if type(self.original_vocab) in [str, unicode]:
            import pdb; pdb.set_trace()
            vocab = getVocabularyRegistry().get(context, self.original_vocab)
        else:
            vocab = self.original_vocab

        if callable(self.hidden_terms):
            self.hidden_terms = self.hidden_terms(contex, vocab)

        return self.wrap_with(vocab, self.hidden_terms)


