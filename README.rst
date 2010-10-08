Introduction
============

Like elephants don't forget anything, so does't
``collective.elephantvocabulary``. It provides a wrapper around for existing
`zope.schema`_ vocabularies and make them not forget anything.

Example usecase would be a vocabulary (source) of users which from certain
point in time wants to hide / deactivate some users for form or listing. But
at the same time you want keep old references to user term working. This is
when ``collective.elephantvocabulary`` comes into the picture. With it you
wrap existing vocabulary of users and provide set of hidden list of users
(term values).


.. contents::


Usage
=====

Some example content and vocabularies

    >>> context = layer.context
    >>> example_vocab = layer.example_vocab
    >>> example_source = layer.example_source

    >>> [i.value for i in example_vocab]
    [1, 2, 3, 4]

Bellow is out wraper method we use to make our existing vocab more 
elephant-like.

    >>> from collective.elephantvocabulary import wrap_vocabulary


In first exampe we pass to our ``wrap_vocabulary`` a vocabulary of 
[1, 2, 3, 4] and we set terms 2 and 3 to hidden. ``wrap_vocabulary``
returns ``VocabularyFactory`` which needs to be called with context
(you could also register it with as utility).

    >>> wrapped_vocab_factory = wrap_vocabulary(example_vocab, [2, 3])
    >>> print wrapped_vocab_factory
    <collective.elephantvocabulary.vocabulary.VocabularyFactory object at ...>

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

Above we see what ``collective.elephantvocabulary`` is all about. When listing
vocabulary hidden terms are not listed. But when item is requested with its
term value then term is also returned. Also length of vocabulary is unchanged.
It still shows original lenght of vocabulary.

We can also call vocabulary by name it was register with ZCA machinery..

    >>> wrapped_vocab2 = wrap_vocabulary('example-vocab', [2, 3])(context)
    >>> [i.value for i in wrapped_vocab2]
    [1, 4]

``hidden_terms`` parameter (second argument we pass to ``wrap_vocabulary``) can
also be callable which expects 2 parameters, ``context`` and ``original vocabulary``.

    >>> def hidden_terms(context, vocab):
    ...     return [1, 4]

    >>> wrapped_vocab3 = wrap_vocabulary(example_vocab, hidden_terms)(context)
    >>> [i.value for i in wrapped_vocab3]
    [2, 3]

``collective.elephantvocabulary`` also works with sources.

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


Todo
====

 * provide list of enabled valued (other way around then hidden_terms is working)
 * provide test for custom wrapper class


History
=======

0.1.1 (2010-10-08)
------------------

 * add dependencies from where we import (using `mr.igor`_) [garbas]
 * add link to ``zope.schema`` which was breaking formating for rst
   formatting [garbas]
 * initial release was broken (missing README.rst) [garbas]

0.1 (2010-10-08)
----------------

 * initial release [garbas]


.. _`Rok Garbas`: http://www.garbas.si
.. _`4teamwork`: http://4teamwork.ch
.. _`zope.schema`: http://pypi.python.org/pypi/zope.schema
.. _`mr.igor`: http://pypi.python.org/pypi/mr.igor
