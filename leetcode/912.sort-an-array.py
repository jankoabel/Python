#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#
# PROBLEM:
# Given an array of integers nums, sort it in ascending order and return it.
# Must run in O(n log n) time — cannot use built-in sort.
# Example: nums=[5,2,3,1] → [1,2,3,5]
#
# APPROACH: Merge Sort.
# Divide array in half, recursively sort each half, then merge.
# Classic O(n log n) divide-and-conquer.

# @lc code=start
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left  = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # Merge two sorted halves
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
        # Time: O(n log n)  Space: O(n)
# @lc code=end
