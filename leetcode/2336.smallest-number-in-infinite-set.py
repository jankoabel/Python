#
# @lc app=leetcode id=2336 lang=python
#
# [2336] Smallest Number in Infinite Set
#
# PROBLEM:
# Start with the infinite set {1,2,3,...}. Implement:
# - popSmallest(): removes and returns the smallest integer
# - addBack(num): adds num back to the set if not already in it
#
# APPROACH: Track a "pointer" for the next un-added-back minimum.
# Use a min-heap for added-back numbers that are smaller than the pointer.

# @lc code=start
import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.pointer = 1       # next number from infinite sequence
        self.added_back = []   # min-heap of numbers added back
        self.in_heap = set()   # avoid duplicates in heap

    def popSmallest(self):
        if self.added_back and self.added_back[0] < self.pointer:
            val = heapq.heappop(self.added_back)
            self.in_heap.discard(val)
            return val
        val = self.pointer
        self.pointer += 1
        return val

    def addBack(self, num):
        if num < self.pointer and num not in self.in_heap:
            heapq.heappush(self.added_back, num)
            self.in_heap.add(num)
        # Time: O(log n) per op  Space: O(n)
# @lc code=end
