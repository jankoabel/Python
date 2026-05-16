#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#
# PROBLEM:
# Given a string s, find the longest palindromic subsequence (not necessarily contiguous).
# Example: s="bbbab" → 4 ("bbbb")  ;  s="cbbd" → 2 ("bb")
#
# APPROACH: 2D DP — interval DP.
# dp[i][j] = length of longest palindromic subsequence in s[i..j]
# If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
# Else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
# Fill by increasing interval length.

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1

        # Fill for lengths 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]
        # Time: O(n^2)  Space: O(n^2)
# @lc code=end
