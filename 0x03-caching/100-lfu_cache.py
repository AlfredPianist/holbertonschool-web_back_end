#!/usr/bin/env python3
"""LFU Caching module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A LFU cache"""

    def __init__(self):
        """Initialization of a cache object, with a separate array of keys"""
        super().__init__()
        self.cache_keys = []
        self.cache_freq = {}

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
            least_freq = min(self.cache_freq.values())
            least_used = [k for k, v in self.cache_freq.items()
                          if v == least_freq]
            if len(least_used) > 1:
                idxs_least_used = sorted(
                    [least_used.index(key) for key in least_used])
                item_out = self.cache_keys.pop(idxs_least_used[0])
            else:
                item_out = least_used[0]
                self.cache_keys.remove(least_used[0])
            print("DISCARD: {}".format(item_out))
            del self.cache_freq[item_out]
            del self.cache_data[item_out]

        self.cache_keys.append(key)
        if self.cache_freq.get(key) is None:
            self.cache_freq[key] = 1
        else:
            self.cache_freq[key] += 1
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
        self.cache_keys.remove(key)
        self.cache_keys.append(key)
        self.cache_freq[key] += 1
        return self.cache_data.get(key)
