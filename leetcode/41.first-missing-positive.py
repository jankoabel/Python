#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive (HARD)
#
# PROBLEM:
# Given an unsorted integer array, find the smallest missing positive integer.
# Must run in O(n) time and use O(1) extra space.
# Example: [3,4,-1,1] → 2 ;  [1,2,0] → 3
#
# APPROACH: Use the array itself as a hash map.
# The answer must be in range [1, n+1] (pigeonhole principle).
# Place each number x in index x-1 if 1 <= x <= n.
# Then scan for the first index i where nums[i] != i+1.

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Step 1: Place each number x at index x-1 (if in valid range)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position nums[i]-1
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]

        # Step 2: Find first position where number is wrong
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1   # missing positive is i+1

        return n + 1   # all 1..n present, so answer is n+1
        # Time: O(n)  Space: O(1)
# @lc code=end
