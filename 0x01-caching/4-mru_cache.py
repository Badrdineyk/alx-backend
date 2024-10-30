#!/usr/bin/env python3
""" 4-mru_cache """

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRU caching system """

    def __init__(self):
        """ Initialize the MRU cache """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key, _ = self.order.popitem(last=True)
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")
            if key in self.cache_data:
                self.order.move_to_end(key)
            self.cache_data[key] = item
            self.order[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key in self.cache_data:
            self.order.move_to_end(key)
            return self.cache_data[key]
        return None
