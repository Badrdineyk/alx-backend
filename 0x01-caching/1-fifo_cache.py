#!/usr/bin/env python3
""" 1-fifo_cache """

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ Initialize the FIFO cache """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key, _ = self.order.popitem(last=False)
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item
            self.order[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
