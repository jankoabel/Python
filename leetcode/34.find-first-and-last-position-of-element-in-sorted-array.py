#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
# PROBLEM:
# Given a sorted array of integers and a target, find the starting and ending
# position of the target. If not found, return [-1, -1].
# Must run in O(log n).
# Example: [5,7,7,8,8,10], target=8 → [3,4]

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search_left(target):
            # Find leftmost index where nums[i] >= target
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid      # keep going left
            return left

        first = binary_search_left(target)

        # Check if target actually exists at that position
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        # Last position = one before the first occurrence of (target+1)
        last = binary_search_left(target + 1) - 1

        return [first, last]
        # Time: O(log n)  Space: O(1)
# @lc code=end
