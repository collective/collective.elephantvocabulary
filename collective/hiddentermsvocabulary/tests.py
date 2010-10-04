import os
import unittest2 as unittest
import doctest

from plone.testing import layered
from collective.hiddentermsvocabulary.testing import HIDDEN_TERMS_VOCAB_LAYER


class TestFasterThanLightTravel(unittest.TestCase):
    layer = HIDDEN_TERMS_VOCAB_LAYER

    def test_something(self):
        self.assertEqual(1, 1)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(
                os.path.join('..', '..', 'README.rst'),
                package='collective.hiddentermsvocabulary'),
                layer = HIDDEN_TERMS_VOCAB_LAYER),
    ])
    return suite

