#
# @lc app=leetcode id=44 lang=python
#
# [44] Wildcard Matching (HARD)
#
# PROBLEM:
# Implement wildcard matching with:
#   '?' matches any single character
#   '*' matches any sequence of characters (including empty)
# Example: s="aa", p="*" → True  ;  s="cb", p="?a" → False
#
# APPROACH: 2D DP.
# dp[i][j] = True if s[:i] matches p[:j]
# - p[j-1]=='*': dp[i][j] = dp[i][j-1] (use * as empty) OR dp[i-1][j] (use * for s[i-1])
# - p[j-1]=='?' or p[j-1]==s[i-1]: dp[i][j] = dp[i-1][j-1]

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

        # '*' can match empty string prefix
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    # Empty sequence OR one more character
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[m][n]
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
