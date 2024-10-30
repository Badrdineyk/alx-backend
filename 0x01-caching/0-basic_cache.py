#!/usr/bin/env python3
""" 0-basic_cache """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache caching system """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
