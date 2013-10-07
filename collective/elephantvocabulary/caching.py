from plone.memoize import ram
from plone.registry.interfaces import IRecordModifiedEvent
from zope.component import adapter
from zope.component import getGlobalSiteManager
from zope.component import getUtility
from zope.component import provideHandler
from zope.interface import implements
from zope.interface import Interface


def _record_from_registry_cachekey(method, self, key):
    """Cache key for the VocabularyFactory.record_from_registry method.
    `key` is the dotted name of the plone.app.registry record.
    """
    return key


class ICachedRecordsRegistry(Interface):
    """Registry for all p.a.registry records that have been RAM cached and
    may need to have their cache invalidated when they change.
    """

    def get_record_keys():
        """Returns keys of all cached p.a.registry records.
        """

    def register_registry_record(record_key):
        """Adds a new p.a.registry record to the registry of cached records.
        """


class CachedRecordsRegistry(object):
    """Global utility that keeps track of registry keys that are used by
    collective.elephantvocabulary as either hidden_terms_from_registry or 
    visible_terms_from_registry, and therefore need to cause a cache
    invalidation if they are modified.
    """
    implements(ICachedRecordsRegistry)

    def __init__(self):
        self.record_keys = []

    def get_record_keys(self):
        return self.record_keys

    def register_registry_record(self, record_key):
        self.record_keys.append(record_key)


# TODO: Move to ZCML
voca_registry = CachedRecordsRegistry()
gsm = getGlobalSiteManager()
gsm.registerUtility(voca_registry, ICachedRecordsRegistry)


def invalidate_records_cache():
    """Invalidates the RAM cache used to cache
    VocabularyFactory.record_from_registry.
    """
    # local import to avoid circular dependency
    from collective.elephantvocabulary import vocabulary
    cache = ram.choose_cache(vocabulary.VocabularyFactory.record_from_registry)
    method_name = '.'.join([vocabulary.__name__, 'record_from_registry'])
    cache.ramcache.invalidate(method_name)
    # TODO: Only invalidate entries with a specific cache key


@adapter(Interface, IRecordModifiedEvent)
def record_modified_handler(record, event):
    """Handler for IRecordModifiedEvent that fires cache invalidation for
    cached registry records if necessary.
    """
    voca_registry = getUtility(ICachedRecordsRegistry)
    for record_name in voca_registry.get_record_keys():
        if record_name.startswith(event.record.interfaceName):
            invalidate_records_cache()


# TODO: Move to ZCML
provideHandler(record_modified_handler)

