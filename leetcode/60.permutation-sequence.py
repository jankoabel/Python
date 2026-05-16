#
# @lc app=leetcode id=60 lang=python
#
# [60] Permutation Sequence (HARD)
#
# PROBLEM:
# Given n and k, return the kth permutation of [1..n] (1-indexed).
# Example: n=3, k=3 → "213"
#
# APPROACH: Factorial number system.
# The first digit has (n-1)! permutations each. Use k-1 to find which digit.
# Reduce to sub-problem.

# @lc code=start
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        digits = list(range(1, n + 1))
        k -= 1  # convert to 0-indexed
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            idx = k // fact
            result.append(str(digits[idx]))
            digits.pop(idx)
            k %= fact

        return ''.join(result)
        # Time: O(n^2) due to list.pop  Space: O(n)
# @lc code=end
