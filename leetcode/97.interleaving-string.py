#
# @lc app=leetcode id=97 lang=python
#
# [97] Interleaving String
#
# PROBLEM:
# Given s1, s2, s3, return true if s3 is formed by an interleaving of s1 and s2.
# An interleaving maintains the relative order of both strings.
# Example: s1="aabcc", s2="dbbca", s3="aadbbcbcac" → True
#
# APPROACH: 2D DP.
# dp[i][j] = True if s3[:i+j] is formed by s1[:i] interleaved with s2[:j]
# Transition: dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or
#                         (dp[i][j-1] and s2[j-1]==s3[i+j-1])

# @lc code=start
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                            (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[m][n]
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
