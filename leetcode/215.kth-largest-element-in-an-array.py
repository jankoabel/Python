#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
# PROBLEM:
# Given an integer array and integer k, return the kth largest element.
# Not the kth distinct element — the kth largest in sorted order.
# Example: [3,2,1,5,6,4], k=2 → 5
#
# APPROACH 1: Min-heap of size k. O(n log k)
# APPROACH 2: QuickSelect (average O(n), worst O(n^2)) — shown below.
# QuickSelect: partition like quicksort, but only recurse into the relevant half.

# @lc code=start
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Min-heap approach: maintain heap of the k largest seen so far
        # The root of the heap is the kth largest
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)   # remove the smallest (keep k largest)
        return heap[0]   # smallest of the k largest = kth largest
        # Time: O(n log k)  Space: O(k)
# @lc code=end
