
from zope.interface import implements
from zope.component import provideUtility
from zope.schema.vocabulary import getVocabularyRegistry
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.interfaces import ISource

from plone.registry import Registry
from plone.registry.interfaces import IRegistry

from plone.testing import Layer
from plone.testing.zca import ZCML_DIRECTIVES

from collective.elephantvocabulary.caching import ICachedRecordsRegistry
from collective.elephantvocabulary.caching import CachedRecordsRegistry

from zope.configuration.xmlconfig import XMLConfig


class ExampleSource(SimpleVocabulary):
    implements(ISource)

    def search(self):
        return [SimpleTerm(1), SimpleTerm(2)]


class ExampleVocabFactory(SimpleVocabulary):
    implements(IVocabularyFactory)
    def __init__(self, context):
        super(ExampleVocabFactory, self).__init__(
                [SimpleTerm(1), SimpleTerm(2),
                 SimpleTerm(3), SimpleTerm(4)])


class VocabularyLayer(Layer):
    defaultBases = (ZCML_DIRECTIVES,)

    def setUp(self):
        import plone.memoize
        XMLConfig('configure.zcml', plone.memoize)()

        self.context = None
        self.example_vocab = SimpleVocabulary.fromValues([1, 2, 3, 4])
        self.example_source = ExampleSource(
                [SimpleTerm(1), SimpleTerm(2),
                 SimpleTerm(3), SimpleTerm(4)])

        registry = getVocabularyRegistry()
        registry.register('example-vocab', ExampleVocabFactory)

        plone_registry = Registry()
        provideUtility(plone_registry, IRegistry)

        voca_registry = CachedRecordsRegistry()
        provideUtility(voca_registry, ICachedRecordsRegistry)


VOCAB_LAYER = VocabularyLayer()
