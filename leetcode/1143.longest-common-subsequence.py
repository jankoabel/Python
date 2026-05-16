#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#
# PROBLEM:
# Given two strings text1 and text2, return the length of their longest common
# subsequence (characters in order but not necessarily contiguous).
# Example: text1="abcde", text2="ace" → 3 (lcs="ace")
#
# APPROACH: 2D DP.
# dp[i][j] = LCS of text1[:i] and text2[:j]
# If chars match: dp[i][j] = dp[i-1][j-1] + 1
# Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
