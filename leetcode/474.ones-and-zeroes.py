#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#
# PROBLEM:
# Given an array of binary strings strs and integers m and n,
# return the size of the largest subset such that there are at most m 0s and n 1s.
# Example: strs=["10","0001","111001","1","0"], m=5, n=3 → 4
#
# APPROACH: 2D 0/1 Knapsack.
# dp[i][j] = max subset size using at most i zeros and j ones.
# For each string (count its 0s and 1s), update dp backwards.

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones  = s.count('1')
            # Traverse backwards to avoid using same string twice
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
        # Time: O(len(strs) * m * n)  Space: O(m * n)
# @lc code=end
