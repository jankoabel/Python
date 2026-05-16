#
# @lc app=leetcode id=1004 lang=python
#
# [1004] Max Consecutive Ones III
#
# PROBLEM:
# Given a binary array nums and an integer k, return the maximum number of
# consecutive 1s if you can flip at most k 0s.
# Example: nums=[1,1,1,0,0,0,1,1,1,1,0], k=2 → 6
#
# APPROACH: Sliding window.
# Expand right. Count zeros in window. If zeros > k, shrink from left.
# Track maximum window size seen.

# @lc code=start
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = zeros = best = 0
        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
        # Time: O(n)  Space: O(1)
# @lc code=end
