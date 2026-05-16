#
# @lc app=leetcode id=315 lang=python
#
# [315] Count of Smaller Numbers After Self (HARD)
#
# PROBLEM:
# Given an integer array nums, return count[i] = number of elements
# to the right of nums[i] that are smaller.
# Example: nums=[5,2,6,1] → [2,1,1,0]
#
# APPROACH: Merge sort — during merge, count how many right-side elements
# are placed before a left-side element.
# Process right-to-left with a sorted list and binary search.

# @lc code=start
import bisect

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_right = []
        result = []

        for num in reversed(nums):
            # Find position where num would be inserted
            pos = bisect.bisect_left(sorted_right, num)
            result.append(pos)  # pos = count of elements < num
            bisect.insort(sorted_right, num)

        return result[::-1]
        # Time: O(n^2) worst case due to insort; O(n log n) with balanced BST
        # Space: O(n)
# @lc code=end
