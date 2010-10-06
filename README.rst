Introduction
============

TODO: intro text

.. contents::


Usage
=====

    >>> context = layer.context
    >>> example_vocab = layer.example_vocab
    >>> example_source = layer.example_source

    >>> [i.value for i in example_vocab]
    [1, 2, 3, 4]

    >>> from collective.hiddentermsvocabulary import wrap_vocabulary

    >>> wrapped_vocab_factory = wrap_vocabulary(example_vocab, [2, 3])
    >>> print wrapped_vocab_factory
    <collective.hiddentermsvocabulary.vocabulary.VocabularyFactory object at ...>

    >>> wrapped_vocab = wrapped_vocab_factory(context)
    >>> [i.value for i in wrapped_vocab]
    [1, 4]

    >>> len(wrapped_vocab) == len(example_vocab)
    True

    >>> 2 in wrapped_vocab
    True

    >>> 5 in wrapped_vocab
    False

    >>> wrapped_vocab.getTerm(3).value
    3

We can also just call vocabulary by name.

    >>> wrapped_vocab2 = wrap_vocabulary('example-vocab', [2, 3])(context)
    >>> [i.value for i in wrapped_vocab2]
    [1, 4]

``hidden_terms`` parameter of ``wrap_vocabulary`` can also be callable which
expects 2 parameters, ``context`` and ``original vocabulary``.

    >>> def hidden_terms(context, vocab):
    ...     return [1, 4]

    >>> wrapped_vocab3 = wrap_vocabulary(example_vocab, hidden_terms)(context)
    >>> [i.value for i in wrapped_vocab3]
    [2, 3]

``collective.hiddentermsvocabulary`` also works with sources.

    >>> [i.value for i in example_source]
    [1, 2, 3, 4]

    >>> [i.value for i in example_source.search()]
    [1, 2]

    >>> wrapped_source = wrap_vocabulary(example_source, [1, 4])(context)
    >>> [i.value for i in wrapped_source.search()]
    [2]


If vocabulary already provides set of hidden terms they are passed to wrapped
vocabulary.

    >>> example_vocab.hidden_terms = [1, 2]
    >>> wrapped_vocab4 = wrap_vocabulary(example_vocab)(context)
    >>> [i.value for i in wrapped_vocab4]
    [3, 4]



Credits
=======

Generously sponsored by `4teamwork`_.

 * `Rok Garbas`_, author


History
=======

0.1 (2010-10-XX)
----------------

 * initial release [garbas]


.. _`Rok Garbas`: http://www.garbas.si
.. _`4teamwork`: http://4teamwork.ch
