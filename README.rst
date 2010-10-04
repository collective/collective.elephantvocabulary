Introduction
============

TODO: intro text

.. contents::


Usage
=====

    
    >>> from collective.hiddentermsvocabulary.vocabulary import HiddenTermsVocabulary
    >>> from zope.schema.vocabulary import SimpleVocabulary

    >>> context = layer['configurationContext']
    >>> vocab = SimpleVocabulary.fromValues([1, 2, 3, 4])

    >>> [i.value for i in vocab]
    [1, 2, 3, 4]

    >>> vocab_with_hidden_terms = HiddenTermsVocabulary(vocab, [2, 3])(context)
    >>> [i.value for i in vocab_with_hidden_terms]
    [1, 4]

    >>> 2 in vocab_with_hidden_terms
    True

    >>> 5 in vocab_with_hidden_terms
    False

    >>> len(vocab_with_hidden_terms)
    4

    >>> from zope.component import provideUtility
    >>> import zope.schema 
    >>> provideUtility(
    ...         vocab,
    ...         zope.schema.interfaces.IVocabularyFactory,
    ...         'existing-vocab',
    ...         context=context)

    >>> import pdb; pdb.set_trace()
    >>> vocab_with_hidden_terms2 = HiddenTermsVocabulary('existing-vocab', [1, 4])(context)
    >>> [i for i in vocab_with_hidden_terms2]
    [2, 3]



    

Credits
=======

 * `Rok Garbas`_, author

 * `4teamwork`_, initial sponsoring 

History
=======

0.1 (2010-10-XX)
----------------

 * initial release [garbas]


.. _`Rok Garbas`: http://www.garbas.si
