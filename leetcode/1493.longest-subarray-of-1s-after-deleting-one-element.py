#
# @lc app=leetcode id=1493 lang=python
#
# [1493] Longest Subarray of 1's After Deleting One Element
#
# PROBLEM:
# Given a binary array nums, return the size of the longest non-empty subarray
# containing only 1s after deleting exactly one element.
# Example: nums=[1,1,0,1] → 3  ;  nums=[0,1,1,1,0,1,1,0,1] → 5
#
# APPROACH: Sliding window allowing at most one 0.
# This is like "Max Consecutive Ones III" with k=1, minus 1 for the deleted element.

# @lc code=start
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = zeros = best = 0
        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            # Window size minus 1 for the mandatory deleted element
            best = max(best, right - left)
        return best
        # Time: O(n)  Space: O(1)
# @lc code=end
