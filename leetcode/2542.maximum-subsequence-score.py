#
# @lc app=leetcode id=2542 lang=python
#
# [2542] Maximum Subsequence Score
#
# PROBLEM:
# You have two arrays nums1 and nums2 of equal length.
# Choose exactly k indices. Score = sum(nums1[chosen]) * min(nums2[chosen]).
# Return the maximum score.
# Example: nums1=[1,3,3,2], nums2=[2,1,3,3], k=3 → 12 (pick i=0,2,3: (1+3+2)*3=18? or (3+3+2)*1)
#
# APPROACH: Sort by nums2 descending. Scan left to right — for each index i,
# nums2[i] is the minimum so far. Keep a min-heap of size k of nums1 values
# to maximize the sum. Score at each i = heap_sum * nums2[i].

# @lc code=start
import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        # Sort pairs by nums2 descending (so nums2[i] is min as we scan)
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        heap = []  # min-heap of nums1 values (size k)
        heap_sum = 0
        best = 0

        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            heap_sum += n1
            if len(heap) > k:
                heap_sum -= heapq.heappop(heap)
            if len(heap) == k:
                best = max(best, heap_sum * n2)

        return best
        # Time: O(n log n + n log k)  Space: O(n + k)
# @lc code=end
