#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
# PROBLEM:
# Given a non-empty array where every element appears twice except one,
# find that single element. Must run in O(n) time and O(1) extra space.
# Example: [4,1,2,1,2] → 4
#
# APPROACH: XOR trick.
# XOR properties: a ^ a = 0,  a ^ 0 = a,  XOR is commutative and associative
# XOR all elements: pairs cancel out, leaving the single element.

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num    # duplicate pairs cancel (x ^ x = 0)
        return result        # only the unique element remains
        # Time: O(n)  Space: O(1)
# @lc code=end
