#
# @lc app=leetcode id=1312 lang=python
#
# [1312] Minimum Insertion Steps to Make a String a Palindrome
#
# PROBLEM:
# Given a string s, in one step you can insert any character at any position.
# Return the minimum number of insertions to make s a palindrome.
# Example: s="zzazz" → 0  ;  s="mbadm" → 2  ;  s="leetcode" → 5
#
# APPROACH: Minimum insertions = len(s) - LPS(s)
# where LPS = longest palindromic subsequence.
# We only need to insert characters for the parts not in the LPS.
# (Same as LCS(s, reversed(s)) which gives LPS length)

# @lc code=start
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # dp[i][j] = LPS length in s[i..j]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return n - dp[0][n-1]
        # Time: O(n^2)  Space: O(n^2)
# @lc code=end
