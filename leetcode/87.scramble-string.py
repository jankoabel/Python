#
# @lc app=leetcode id=87 lang=python
#
# [87] Scramble String (HARD)
#
# PROBLEM:
# A string s1 is a scramble of s2 if we can split s1 into two parts and either
# - both halves match (in order) the corresponding split of s2, or
# - one half is swapped.
# Return true if s1 is a scramble of s2.
# Example: s1="great", s2="rgeat" → True
#
# APPROACH: Recursion with memoization.
# For each split length k (1 to n-1):
#   - No swap: isScramble(s1[:k], s2[:k]) and isScramble(s1[k:], s2[k:])
#   - Swap: isScramble(s1[:k], s2[n-k:]) and isScramble(s1[k:], s2[:n-k])

# @lc code=start
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}

        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for k in range(1, n):
                # No swap
                if dp(a[:k], b[:k]) and dp(a[k:], b[k:]):
                    memo[(a, b)] = True
                    return True
                # Swap
                if dp(a[:k], b[n-k:]) and dp(a[k:], b[:n-k]):
                    memo[(a, b)] = True
                    return True
            memo[(a, b)] = False
            return False

        return dp(s1, s2)
        # Time: O(n^4) with memoization  Space: O(n^3)
# @lc code=end
