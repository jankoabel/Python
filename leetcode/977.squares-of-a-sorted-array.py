#
# @lc app=leetcode id=977 lang=python
#
# [977] Squares of a Sorted Array
#
# PROBLEM:
# Given an integer array sorted in non-decreasing order, return an array of
# the squares of each number, also in non-decreasing order.
# Example: nums=[-4,-1,0,3,10] → [0,1,9,16,100]
#
# APPROACH: Two pointers from both ends.
# The largest square is always at one of the ends (most negative or largest positive).
# Fill result from right to left.

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # fill result from the back

        while left <= right:
            l_sq = nums[left] ** 2
            r_sq = nums[right] ** 2
            if l_sq > r_sq:
                result[pos] = l_sq
                left += 1
            else:
                result[pos] = r_sq
                right -= 1
            pos -= 1

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
