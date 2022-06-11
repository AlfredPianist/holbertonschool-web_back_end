#!/usr/bin/env python3
"""FIFO Caching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO cache"""

    def __init__(self):
        """Initialization of a cache object, with a separate array of keys"""
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """Puts a key into the cache.
        Args:
            key (`str`): The key of the key-value pair to include in the cache.
            value (`str`): The value of the key-value pair to include in the
                cache.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            item_out = self.cache_keys.pop(0)
            print("DISCARD: {}".format(item_out))
            del self.cache_data[item_out]

        self.cache_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value of the key.
        Args:
            key (`str`): The key of the key-value pair to include in the cache.
        Returns:
            `str`: The value of the key in the cache. `None` if non existent.
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
