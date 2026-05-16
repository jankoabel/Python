#
# @lc app=leetcode id=862 lang=python
#
# [862] Shortest Subarray with Sum at Least K (HARD)
#
# PROBLEM:
# Given an integer array nums (possibly negative) and integer k,
# return the length of the shortest subarray with sum >= k. Return -1 if none.
# Example: nums=[2,-1,2], k=3 → 3
#
# APPROACH: Prefix sums + monotonic deque.
# prefix[j] - prefix[i] = sum(nums[i..j-1]).
# We want the smallest j-i where prefix[j] - prefix[i] >= k.
# Maintain an increasing deque of prefix indices.
# For each j: while deque front satisfies condition, update answer and pop.

# @lc code=start
from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        dq = deque()  # monotonically increasing prefix values (indices)
        result = float('inf')

        for j in range(n + 1):
            # Pop from front: valid subarrays with sum >= k
            while dq and prefix[j] - prefix[dq[0]] >= k:
                result = min(result, j - dq.popleft())
            # Pop from back: maintain increasing order
            while dq and prefix[dq[-1]] >= prefix[j]:
                dq.pop()
            dq.append(j)

        return result if result < float('inf') else -1
        # Time: O(n)  Space: O(n)
# @lc code=end
