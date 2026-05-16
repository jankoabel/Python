#
# @lc app=leetcode id=1439 lang=python
#
# [1439] Find the Kth Smallest Sum of a Matrix With Sorted Rows (HARD)
#
# PROBLEM:
# Given an m×n sorted matrix, choose one element from each row.
# Return the kth smallest sum.
# Example: mat=[[1,3,11],[2,4,6]], k=5 → 7
#
# APPROACH: Use a min-heap. Start with the smallest combination (all first elements).
# At each step, expand by incrementing one index at a time.
# Or: iteratively merge two rows using a heap of k smallest sums.

# @lc code=start
import heapq

class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Merge rows one at a time, keeping only k smallest sums
        current = [0]

        for row in mat:
            # Combine current sums with this row
            heap = []
            for prev_sum in current:
                for val in row:
                    heapq.heappush(heap, prev_sum + val)
            # Keep only k smallest
            current = []
            for _ in range(min(k, len(heap))):
                current.append(heapq.heappop(heap))

        return current[k - 1]
        # Time: O(m * n * k * log(n*k))  Space: O(k)
# @lc code=end
