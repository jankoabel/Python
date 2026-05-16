#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#
# PROBLEM:
# Given an array with values 0 (red), 1 (white), 2 (blue),
# sort in-place so all 0s come first, then 1s, then 2s.
# Must solve in one pass with O(1) extra space.
# Example: [2,0,2,1,1,0] → [0,0,1,1,2,2]
#
# APPROACH: Dutch National Flag algorithm — 3 pointers.
# low: next position for 0
# mid: current element being examined
# high: next position for 2

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1    # 0 placed correctly
                mid += 1    # element at mid was previously sorted (it was 1)
            elif nums[mid] == 1:
                mid += 1    # 1 is already in the right section, just advance
            else:           # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1   # 2 placed at end; don't advance mid (swapped element unchecked)
        # Time: O(n)  Space: O(1)
# @lc code=end
