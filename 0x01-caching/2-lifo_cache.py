#!/usr/bin/env python3
""" 2-lifo_cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = self.keys.pop()
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
