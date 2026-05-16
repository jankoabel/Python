#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
# PROBLEM:
# Given a non-negative integer x, return the square root of x rounded down to integer.
# Do NOT use any built-in exponent functions.
# Example: x=8 → 2 (because sqrt(8) ≈ 2.828, floor = 2)
#
# APPROACH: Binary search on answer in range [0, x].
# Find largest k such that k*k <= x.

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x   # 0 and 1 are their own square roots

        left, right = 1, x // 2   # sqrt(x) <= x//2 for x >= 4

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1     # mid might be the answer, but try larger
            else:
                right = mid - 1   # mid is too large

        return right   # right is the floor of sqrt(x)
        # Time: O(log x)  Space: O(1)
# @lc code=end
