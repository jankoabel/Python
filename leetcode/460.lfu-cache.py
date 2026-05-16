#
# @lc app=leetcode id=460 lang=python
#
# [460] LFU Cache (HARD)
#
# PROBLEM:
# Design a Least Frequently Used (LFU) cache. When capacity is reached,
# the least frequently used item is removed (ties broken by LRU).
# Implement get(key) and put(key, value), both in O(1).
#
# APPROACH: Three hash maps:
# - key_to_val: key → value
# - key_to_freq: key → frequency
# - freq_to_keys: freq → OrderedDict of keys (LRU order within same freq)
# Track min_freq for O(1) eviction.

# @lc code=start
from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_val  = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)  # freq → {key: None}
        self.min_freq = 0

    def _update(self, key):
        freq = self.key_to_freq[key]
        self.key_to_freq[key] = freq + 1
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key):
        if key not in self.key_to_val:
            return -1
        self._update(key)
        return self.key_to_val[key]

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update(key)
        else:
            if len(self.key_to_val) == self.capacity:
                # Evict LRU among minimum frequency
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val[evict_key]
                del self.key_to_freq[evict_key]
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
        # Time: O(1) each  Space: O(capacity)
# @lc code=end
