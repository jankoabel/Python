#
# @lc app=leetcode id=664 lang=python
#
# [664] Strange Printer (HARD)
#
# PROBLEM:
# A printer can print a sequence of same characters in one turn, and
# can overprint previous characters. Find minimum turns to print string s.
# Example: s="aaabbb" → 2  ;  s="aba" → 2
#
# APPROACH: Interval DP.
# dp[i][j] = min turns to print s[i..j].
# Key insight: if s[i] == s[k] for some k in (i,j], we can print s[i..k]
# in one turn that also covers position k (saving 1 turn).
# dp[i][j] = min over k of dp[i][k-1] + dp[k][j] (where we split)
# But if s[i]==s[j]: dp[i][j] = dp[i][j-1] (merge the last char into first group)

# @lc code=start
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j-1] + 1  # print s[j] separately
                for k in range(i, j):
                    if s[k] == s[j]:
                        # Merge s[j] into s[k]'s turn
                        val = dp[i][k] + (dp[k+1][j-1] if k+1 <= j-1 else 0)
                        dp[i][j] = min(dp[i][j], val)

        return dp[0][n-1]
        # Time: O(n^3)  Space: O(n^2)
# @lc code=end
