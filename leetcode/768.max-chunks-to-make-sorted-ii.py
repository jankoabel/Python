#
# @lc app=leetcode id=768 lang=python
#
# [768] Max Chunks To Make Sorted II (HARD)
#
# PROBLEM:
# Given an array arr, split it into chunks so that when sorted individually
# and concatenated, the whole array is sorted. Return max number of chunks.
# Example: arr=[5,4,3,2,1] → 1  ;  arr=[2,1,3,4,4] → 4
#
# APPROACH: A chunk boundary at i is valid if max(arr[0..i]) <= min(arr[i+1..n-1]).
# Precompute prefix maxes and suffix mins. Count valid boundaries.

# @lc code=start
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], arr[i])
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], arr[i])

        chunks = 1
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i+1]:
                chunks += 1

        return chunks
        # Time: O(n)  Space: O(n)
# @lc code=end
