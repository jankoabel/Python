#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
# PROBLEM:
# Given an array of positive integers and a target, find the minimal length
# subarray whose sum >= target. Return 0 if no such subarray exists.
# Example: target=7, [2,3,1,2,4,3] → 2 (subarray [4,3])
#
# APPROACH: Sliding window — expand right, shrink left when sum >= target.
# Both pointers only move forward → O(n) total.

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]   # expand window

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]  # shrink window from left
                left += 1

        return 0 if min_len == float('inf') else min_len
        # Time: O(n)  Space: O(1)
# @lc code=end
