from plone.memoize import ram
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import getVocabularyRegistry

from collective.elephantvocabulary.base import WrapperBase
from collective.elephantvocabulary.caching import _record_from_registry_cachekey
from collective.elephantvocabulary.caching import ICachedRecordsRegistry


try:
    from plone.registry.interfaces import IRegistry
    PLONE_REGISTRY = True
except:
    PLONE_REGISTRY = False


class VocabularyFactory(object):

    implements(IVocabularyFactory, IContextSourceBinder)

    def __init__(self, vocab,
                 visible_terms=None,
                 visible_terms_from_registry=None,
                 hidden_terms=None,
                 hidden_terms_from_registry=None,
                 wrapper_class=WrapperBase):
        self.vocab = vocab
        self.visible_terms = visible_terms
        self.visible_terms_from_registry = visible_terms_from_registry
        self.hidden_terms = hidden_terms
        self.hidden_terms_from_registry = hidden_terms_from_registry
        self.wrapper_class = wrapper_class

        voca_registry = getUtility(ICachedRecordsRegistry)
        if self.hidden_terms_from_registry is not None:
            voca_registry.register_registry_record(
                self.hidden_terms_from_registry)
        if self.visible_terms_from_registry is not None:
            voca_registry.register_registry_record(
                self.visible_terms_from_registry)


    @ram.cache(_record_from_registry_cachekey)
    def record_from_registry(self, key):
        registry = getUtility(IRegistry)
        record = registry.get(key, None)
        return record

    def __call__(self, context):

        if isinstance(self.vocab, basestring):
            original_vocab = getVocabularyRegistry().get(context, self.vocab)
        else:
            original_vocab = self.vocab

        if callable(self.visible_terms):
            self.visible_terms = self.visible_terms(context, original_vocab)

        if self.visible_terms_from_registry is not None and PLONE_REGISTRY:
            record = self.record_from_registry(self.visible_terms_from_registry)
            if record and type(record) == list:
                if type(self.visible_terms) == list:
                    for term in record:
                        if not term in self.visible_terms:
                            self.visible_terms.append(term)
                else:
                    self.visible_terms = record

        if getattr(original_vocab, 'visible_terms', False) and \
                isinstance(original_vocab.visible_terms, list):
            if self.visible_terms is None:
                self.visible_terms = original_vocab.visible_terms
            else:
                self.visible_terms += original_vocab.visible_terms

        if callable(self.hidden_terms):
            self.hidden_terms = self.hidden_terms(context, original_vocab)

        if self.hidden_terms_from_registry is not None and PLONE_REGISTRY:
            record = self.record_from_registry(self.hidden_terms_from_registry)
            if record and type(record) == list:
                if type(self.hidden_terms) == list:
                    for term in record:
                        if not term in self.hidden_terms:
                            self.hidden_terms.append(term)
                else:
                    self.hidden_terms = record

        if getattr(original_vocab, 'hidden_terms', False) and \
                isinstance(original_vocab.hidden_terms, list):
            if self.hidden_terms is None:
                self.hidden_terms = original_vocab.hidden_terms
            else:
                self.hidden_terms += original_vocab.hidden_terms

        return self.wrapper_class(original_vocab,
                    visible_terms=self.visible_terms,
                    hidden_terms=self.hidden_terms)
