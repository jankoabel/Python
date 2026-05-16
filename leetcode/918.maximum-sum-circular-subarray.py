#
# @lc app=leetcode id=918 lang=python
#
# [918] Maximum Sum Circular Subarray
#
# PROBLEM:
# Given a circular integer array nums, return the maximum possible subarray sum.
# A circular subarray can wrap around from the end to the start.
# Example: nums=[1,-2,3,-2] → 3  ;  nums=[5,-3,5] → 10
#
# APPROACH: Two cases:
# 1. Max subarray doesn't wrap → Kadane's algorithm
# 2. Max subarray wraps → total_sum - min_subarray_sum
# Answer is max of both. Edge case: if all negative, answer is max element.

# @lc code=start
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)

        # Kadane for maximum subarray
        max_sum = cur_max = nums[0]
        # Kadane for minimum subarray
        min_sum = cur_min = nums[0]

        for num in nums[1:]:
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)

        # If all numbers are negative, max_sum is the least-negative
        if max_sum < 0:
            return max_sum
        # Circular case: total - min_subarray
        return max(max_sum, total - min_sum)
        # Time: O(n)  Space: O(1)
# @lc code=end
