#
# @lc app=leetcode id=503 lang=python
#
# [503] Next Greater Element II
#
# PROBLEM:
# Given a circular array nums, find the next greater number for every element.
# The next greater number of a number x is the first greater number traversing
# the array in a circular order.
# Example: [1,2,1] → [2,-1,2]
#
# APPROACH: Monotonic stack. Simulate two passes through the array (by going 0..2n).
# Use modulo to wrap indices. Only push actual indices on the stack.

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1] * n
        stack = []  # stores indices, monotonic decreasing by value

        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]
            if i < n:
                stack.append(idx)

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
