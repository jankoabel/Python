#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#
# PROBLEM:
# Design a data structure that follows the Least Recently Used (LRU) cache policy.
# Implement LRUCache(capacity), get(key), put(key, value).
# get(key): return value if exists, else -1. Marks key as recently used.
# put(key, value): insert/update. If capacity exceeded, evict LRU key.
# Both operations must be O(1).
#
# APPROACH: Hash map + Doubly Linked List.
# Map: key → node (O(1) lookup)
# DLL: maintains order (head = most recent, tail = least recent)
# On access/insert: move node to head.
# On eviction: remove from tail.

# @lc code=start
class LRUCache(object):
    class Node:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}   # key → Node
        # Sentinel head (MRU end) and tail (LRU end)
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_front(node)   # mark as most recently used
            return node.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = self.Node(key, value)
        self.cache[key] = node
        self._insert_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev      # least recently used
            self._remove(lru)
            del self.cache[lru.key]
    # All operations: Time O(1)  Space O(capacity)
# @lc code=end
