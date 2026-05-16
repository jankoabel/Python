#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching (HARD)
#
# PROBLEM:
# Given input string s and pattern p, implement regex matching with:
#   '.' matches any single character
#   '*' matches zero or more of the preceding element
# Example: s="aa", p="a*" → True  ;  s="ab", p=".*" → True
#
# APPROACH: 2D DP.
# dp[i][j] = True if s[:i] matches p[:j]
# - If p[j-1] == '*': either skip (0 occurrences) dp[i][j-2],
#                     or use it: p[j-2] matches s[i-1] and dp[i-1][j]
# - Else: chars match and dp[i-1][j-1]

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Empty string can match patterns like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    # Skip preceding element (0 occurrences)
                    dp[i][j] = dp[i][j-2]
                    # Or use preceding element if it matches s[i-1]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[m][n]
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
