Introduction
============

Like elephants don't forget anything, so does not
``collective.elephantvocabulary``. It provides a wrapper around for existing
`zope.schema`_ vocabularies and make them not forget anything.

Example usecase would be a vocabulary (source) of users which from certain
point in time wants to hide / deactivate some users for form or listing. But
at the same time you want keep old references to user term working. This is
where ``collective.elephantvocabulary`` comes into the picture. With it you
wrap existing vocabulary of users and provide set of hidden list of users
(term values).


.. contents::

.. _`zope.schema`: http://pypi.python.org/pypi/zope.schema
