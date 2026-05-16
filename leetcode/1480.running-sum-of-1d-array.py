#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#
# PROBLEM:
# Given an array nums, return the running sum where runningSum[i] = sum(nums[0..i]).
# Example: nums=[1,2,3,4] → [1,3,6,10]
#
# APPROACH: Prefix sum — add each element to the accumulated total.

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
        # Time: O(n)  Space: O(1) in-place
# @lc code=end
