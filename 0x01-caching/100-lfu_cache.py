#!/usr/bin/env python3
""" LFU Caching module
"""

from base_caching import BaseCaching
from collections import defaultdict
import heapq


class LFUCache(BaseCaching):
    """LFU caching system"""

    def __init__(self):
        """Initialize LFUCache"""
        super().__init__()
        self.freq = defaultdict(int)
        self.min_heap = []
        self.key_heap = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            heapq.heappush(self.min_heap, (self.freq[key], key))
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._evict()
        self.cache_data[key] = item
        self.freq[key] += 1
        heapq.heappush(self.min_heap, (self.freq[key], key))
        self.key_heap[key] = self.freq[key]

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        heapq.heappush(self.min_heap, (self.freq[key], key))
        return self.cache_data[key]

    def _evict(self):
        """Evict the least frequently used item"""
        while self.min_heap:
            freq, key = heapq.heappop(self.min_heap)
            if self.freq[key] == freq:
                print(f"DISCARD: {key}")
                del self.cache_data[key]
                del self.freq[key]
                return
