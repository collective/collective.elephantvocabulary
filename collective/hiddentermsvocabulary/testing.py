import zope.component
from zope.configuration import xmlconfig
from plone.testing import Layer
from plone.testing.zca import ZCML_DIRECTIVES


class HiddenTermsVocabularyLayer(Layer):
    defaultBases = (ZCML_DIRECTIVES,)

    def setUp(self):
        xmlconfig.file('configure.zcml',
                       zope.component,
                       context=self['configurationContext'])


HIDDEN_TERMS_VOCAB_LAYER = HiddenTermsVocabularyLayer()
