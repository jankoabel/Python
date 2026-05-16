#
# @lc app=leetcode id=432 lang=python
#
# [432] All O`one Data Structure (HARD)
#
# PROBLEM:
# Design a data structure with O(1) time for:
# - inc(key): increment key's count
# - dec(key): decrement key's count (remove if 0)
# - getMaxKey(): return any key with max count
# - getMinKey(): return any key with min count
#
# APPROACH: Doubly linked list of Bucket nodes, each holding a count and set of keys.
# Buckets are ordered by count. Hash map key → bucket.

# @lc code=start
class Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = self.next = None

class AllOne(object):

    def __init__(self):
        self.head = Bucket(0)   # sentinel min
        self.tail = Bucket(0)   # sentinel max
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_bucket = {}

    def _insert_after(self, bucket, count):
        new = Bucket(count)
        new.prev, new.next = bucket, bucket.next
        bucket.next.prev = new
        bucket.next = new
        return new

    def _remove_bucket(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev

    def inc(self, key):
        if key not in self.key_to_bucket:
            # Add to bucket with count 1 (create if needed)
            if self.head.next.count != 1:
                self._insert_after(self.head, 1)
            self.head.next.keys.add(key)
            self.key_to_bucket[key] = self.head.next
        else:
            curr = self.key_to_bucket[key]
            nxt = curr.next
            if nxt == self.tail or nxt.count != curr.count + 1:
                nxt = self._insert_after(curr, curr.count + 1)
            nxt.keys.add(key)
            self.key_to_bucket[key] = nxt
            curr.keys.discard(key)
            if not curr.keys:
                self._remove_bucket(curr)

    def dec(self, key):
        curr = self.key_to_bucket[key]
        if curr.count == 1:
            del self.key_to_bucket[key]
        else:
            prv = curr.prev
            if prv == self.head or prv.count != curr.count - 1:
                prv = self._insert_after(prv, curr.count - 1)
            prv.keys.add(key)
            self.key_to_bucket[key] = prv
        curr.keys.discard(key)
        if not curr.keys:
            self._remove_bucket(curr)

    def getMaxKey(self):
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self):
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""
        # Time: O(1) each  Space: O(n)
# @lc code=end
