#
# @lc app=leetcode id=1137 lang=python
#
# [1137] N-th Tribonacci Number
#
# PROBLEM:
# T0=0, T1=1, T2=1. Tn+3 = Tn + Tn+1 + Tn+2.
# Return the value of Tn.
# Example: n=4 → 4  ;  n=25 → 1389537
#
# APPROACH: Iterative DP with three variables (O(1) space).

# @lc code=start
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n <= 2: return 1
        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c
        # Time: O(n)  Space: O(1)
# @lc code=end
