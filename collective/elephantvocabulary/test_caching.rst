Test caching of registry records used to populate vocabularies
==============================================================

Some example content and vocabularies

    >>> context = layer.context
    >>> example_vocab = layer.example_vocab
    >>> example_source = layer.example_source
    >>> [i.value for i in example_vocab]
    [1, 2, 3, 4]


Some example registry records

    >>> from zope.component import getUtility
    >>> from plone.registry import field
    >>> from plone.registry import Record
    >>> from plone.registry.interfaces import IRegistry
    >>> from collective.elephantvocabulary import wrap_vocabulary

    >>> example_registry_record = Record(
    ...         field.List(title=u"Test", min_length=0, max_length=10,
    ...                    value_type=field.Int(title=u"Value")))
    >>> example_registry_record.value = [1, 2]

    >>> registry = getUtility(IRegistry)
    >>> registry.records['example.hidden_terms'] = example_registry_record
    >>> registry.records['example.visible_terms'] = example_registry_record


We create a vocabulary factory populated with hidden terms from a registry
record:

    >>> wrapped_vocab_factory = wrap_vocabulary(example_vocab,
    ...         hidden_terms_from_registry='example.hidden_terms')

    >>> wrapped_vocab1 = wrapped_vocab_factory(context)
    >>> [i.value for i in wrapped_vocab1]
    [3, 4]

If we now change the contents of the registry record to hide all values,

    >>> registry.records['example.hidden_terms'].value = [1, 2, 3, 4]

nothing seems to change in the vocabulary -  because access to registry records
is cached:

    >>> [i.value for i in wrapped_vocab1]
    [3, 4]

Only once we invalidate the cache the new terms are reflected in the vocabulary:

    >>> from collective.elephantvocabulary.caching import invalidate_records_cache
    >>> invalidate_records_cache()
    >>> wrapped_vocab1 = wrapped_vocab_factory(context)
    >>> [i.value for i in wrapped_vocab1]
    []
