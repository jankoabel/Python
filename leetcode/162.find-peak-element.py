#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#
# PROBLEM:
# A peak element is one that is strictly greater than its neighbors.
# Given an array, return the index of any peak element.
# Assume nums[-1] = nums[n] = -infinity. Must run in O(log n).
# Example: [1,2,3,1] → 2  ;  [1,2,1,3,5,6,4] → 5 (index of 6)
#
# APPROACH: Binary search — always move toward the uphill side.
# If nums[mid] < nums[mid+1], a peak exists on the right → go right.
# Otherwise → go left (peak exists at mid or left).

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1    # slope goes up → peak is to the right
            else:
                right = mid       # slope goes down (or flat) → peak is at mid or left

        return left   # left == right == peak index
        # Time: O(log n)  Space: O(1)
# @lc code=end
