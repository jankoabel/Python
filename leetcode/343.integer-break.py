#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#
# PROBLEM:
# Given an integer n, break it into at least 2 positive integers that sum to n,
# and maximize their product.
# Example: n=2 → 1  ;  n=10 → 36 (3+3+4=10, 3*3*4=36)
#
# APPROACH: Math/Greedy.
# Key insight: 3s maximize the product. Never use 1s. Use 2s only if remainder is 2 or 4.
# - If n % 3 == 0: all 3s → 3^(n//3)
# - If n % 3 == 1: replace one 3 with two 2s → 3^(n//3 - 1) * 4
# - If n % 3 == 2: use one 2 → 3^(n//3) * 2

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2

        threes = n // 3
        remainder = n % 3

        if remainder == 0:
            return 3 ** threes
        elif remainder == 1:
            # 3+1 gives 3*1=3, but 2+2 gives 2*2=4 → replace one 3 with two 2s
            return 3 ** (threes - 1) * 4
        else:  # remainder == 2
            return 3 ** threes * 2
        # Time: O(1)  Space: O(1)
# @lc code=end
