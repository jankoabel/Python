#
# @lc app=leetcode id=115 lang=python
#
# [115] Distinct Subsequences (HARD)
#
# PROBLEM:
# Given strings s and t, return the number of distinct subsequences of s that
# equal t.
# Example: s="rabbbit", t="rabbit" → 3
#
# APPROACH: 2D DP.
# dp[i][j] = number of ways s[:i] contains t[:j] as a subsequence.
# If s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#   (use this char OR skip it)
# Else: dp[i][j] = dp[i-1][j] (skip s[i-1])

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty t can be matched by any prefix of s in exactly 1 way
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j]  # always skip s[i-1]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]  # also use s[i-1] to match t[j-1]

        return dp[m][n]
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
