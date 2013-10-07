Tests related to getting terms from registry
============================================

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

    >>> example_registry_record = Record(
    ...         field.List(title=u"Test", min_length=0, max_length=10,
    ...                    value_type=field.Int(title=u"Value")))
    >>> example_registry_record.value = [1, 2]

    >>> registry = getUtility(IRegistry)
    >>> registry.records['example.hidden_terms'] = example_registry_record
    >>> registry.records['example.visible_terms'] = example_registry_record


    >>> from collective.elephantvocabulary import wrap_vocabulary

    >>> wrapped_vocab_factory = wrap_vocabulary(example_vocab,
    ...         hidden_terms_from_registry='example.hidden_terms')

    >>> wrapped_vocab1 = wrapped_vocab_factory(context)

Hidden terms should not grow after instanciating the vocab factory several
times:

    >>> wrapped_vocab_factory.hidden_terms
    [1, 2]

    >>> wrapped_vocab2 = wrapped_vocab_factory(context)

    >>> wrapped_vocab_factory.hidden_terms
    [1, 2]


Same for visible terms - visible terms should not grow after instanciating the
vocab factory several times:


    >>> wrapped_vocab_factory = wrap_vocabulary(example_vocab,
    ...         visible_terms_from_registry='example.visible_terms')

    >>> wrapped_vocab1 = wrapped_vocab_factory(context)


    >>> wrapped_vocab_factory.visible_terms
    [1, 2]

    >>> wrapped_vocab2 = wrapped_vocab_factory(context)

    >>> wrapped_vocab_factory.visible_terms
    [1, 2]
