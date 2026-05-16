#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#
# PROBLEM:
# Calculate the sum of two integers a and b without using + or -.
# Example: a=1, b=2 → 3  ;  a=-2, b=3 → 1
#
# APPROACH: Bit manipulation.
# XOR gives the sum without carry. AND<<1 gives the carry bits.
# Repeat until no carry. Python integers are unbounded so mask to 32 bits.

# @lc code=start
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        while b & MASK:
            # carry bits, then sum without carry
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        # sign-extend if result is negative in 32-bit
        return a if a < 0x80000000 else ~(a ^ MASK)
        # Time: O(1)  Space: O(1)
# @lc code=end
