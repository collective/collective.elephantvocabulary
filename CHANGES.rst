History
=======

0.2.3 (unreleased)
------------------

 * Don't memoize the persistent plone.registry utility. This avoids issues
   with object access across different ZODB connections (see issue #2).
   [lgraf]

 * Split the ``README.rst`` up into several files. Put the testing
   part in ``tests.rst`` in the main directory so this test file can also
   be found when we are distributed on PyPI. [maurits]

0.2.2 (2010-10-12)
------------------

 * support for other type of vocabs (IVocabulary, IIterableSource) [garbas]
 * BUG(Fixed): registry should be not be loaded at __init__ time [garbas]

0.2.1 (2010-10-11)
------------------

 * new parameters ``visible_terms_from_registry`` and
   ``hidden_terms_from_registry`` which reads values directly from
   `plone.registry`_. [garbas]

0.2 (2010-10-11)
----------------

 * visible_terms parameter added to ``wrap_vocabulary``, by default visible_terms
   and hidden_terms work "together" (via WrapperBase) [garbas]

0.1.3 (2010-10-11)
------------------

 * marking wrapper vocabularies with IElephantVocabulary interface [garbas]

0.1.2 (2010-10-08)
------------------

 * misspelled dependency, feeling silly [garbas]

0.1.1 (2010-10-08)
------------------

 * add dependencies from where we import (using `mr.igor`_) [garbas]
 * add link to ``zope.schema`` which was breaking formating for rst
   formatting [garbas]
 * initial release was broken (missing README.rst) [garbas]

0.1 (2010-10-08)
----------------

 * initial release [garbas]

.. _`mr.igor`: http://pypi.python.org/pypi/mr.igor
.. _`plone.registry`: http://pypi.python.org/pypi/plone.registry
