#
# @lc app=leetcode id=583 lang=python
#
# [583] Delete Operation for Two Strings
#
# PROBLEM:
# Given two strings word1 and word2, return the minimum number of steps to make
# them the same, where each step deletes one character from either string.
# Example: word1="sea", word2="eat" → 2 (delete 's' from sea, delete 't' from eat)
#
# APPROACH: Find LCS (Longest Common Subsequence).
# Characters in the LCS don't need to be deleted.
# Answer = len(word1) + len(word2) - 2 * LCS(word1, word2)

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        # dp[i][j] = LCS length for word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lcs = dp[m][n]
        return (m - lcs) + (n - lcs)
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
