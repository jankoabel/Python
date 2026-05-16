#
# @lc app=leetcode id=1808 lang=python
#
# [1808] Maximize Number of Nice Divisors (HARD)
#
# PROBLEM:
# A divisor of n is "nice" if it divides n and n/divisor has exactly primeFactors prime factors.
# Given primeFactors, find max number of nice divisors (mod 10^9+7).
# This is equivalent to: split primeFactors into groups to maximize product.
# Example: primeFactors=5 → 6 (split as 2+3, product=6)
#
# APPROACH: Same as "Integer Break" — split into 3s maximize product.
# Use fast modular exponentiation.

# @lc code=start
class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = primeFactors

        if n <= 3: return n
        if n % 3 == 0:
            return pow(3, n // 3, MOD)
        elif n % 3 == 1:
            return pow(3, n // 3 - 1, MOD) * 4 % MOD
        else:
            return pow(3, n // 3, MOD) * 2 % MOD
        # Time: O(log n)  Space: O(1)
# @lc code=end
