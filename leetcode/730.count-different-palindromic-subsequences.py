#
# @lc app=leetcode id=730 lang=python
#
# [730] Count Different Palindromic Subsequences (HARD)
#
# PROBLEM:
# Given a string s, return the number of distinct palindromic subsequences.
# Answer modulo 10^9 + 7.
# Example: s="bccb" → 6 ("b","c","bb","cc","bcb","bccb")
#
# APPROACH: Interval DP.
# dp[i][j] = number of distinct palindromic subsequences in s[i..j].
# If s[i] != s[j]: dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1] (inclusion-exclusion)
# If s[i] == s[j]: find leftmost/rightmost occurrence of s[i] inside (i,j).
#   - No inner occurrence: dp[i][j] = dp[i+1][j-1] * 2 + 2
#   - One inner occurrence: dp[i][j] = dp[i+1][j-1] * 2 + 1
#   - Two or more: dp[i][j] = dp[i+1][j-1] * 2 - dp[lo+1][hi-1]

# @lc code=start
class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                else:
                    lo, hi = i + 1, j - 1
                    while lo <= hi and s[lo] != s[i]: lo += 1
                    while lo <= hi and s[hi] != s[i]: hi -= 1
                    if lo > hi:
                        dp[i][j] = dp[i+1][j-1] * 2 + 2
                    elif lo == hi:
                        dp[i][j] = dp[i+1][j-1] * 2 + 1
                    else:
                        dp[i][j] = dp[i+1][j-1] * 2 - dp[lo+1][hi-1]
                dp[i][j] %= MOD

        return dp[0][n-1]
        # Time: O(n^3)  Space: O(n^2)
# @lc code=end
