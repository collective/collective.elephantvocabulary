from collective.elephantvocabulary.vocabulary import VocabularyFactory
from collective.elephantvocabulary.hidden import WrapperHidden


def wrap_vocabulary(original_vocab, hidden_terms=[], wrapper=WrapperHidden):
    return VocabularyFactory(original_vocab, hidden_terms, wrapper)


__all__ = ['wrap_vocabulary']
