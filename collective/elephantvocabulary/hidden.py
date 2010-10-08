

class WrapperHidden(object):

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
