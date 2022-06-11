#!/usr/bin/env python3
"""Basic Caching module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache"""

    def put(self, key, item):
        """Puts a key into the cache.
        Args:
            key (`str`): The key of the key-value pair to include in the cache.
            value (`str`): The value of the key-value pair to include in the
                cache.
        """
        if key and item:
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
