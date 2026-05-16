#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#
# PROBLEM:
# Given integer n, return the number of structurally unique BSTs
# that store values 1 to n.
# Example: n=3 → 5
#
# APPROACH: Catalan number via DP.
# dp[n] = number of unique BSTs with n nodes
# dp[i] = sum of dp[k-1] * dp[i-k] for k from 1 to i
# (k = root, dp[k-1] = left subtree options, dp[i-k] = right subtree options)

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1   # empty tree: 1 way
        dp[1] = 1   # single node: 1 way

        for i in range(2, n + 1):
            for k in range(1, i + 1):
                # k is the root; left subtree has k-1 nodes, right has i-k nodes
                dp[i] += dp[k - 1] * dp[i - k]

        return dp[n]
        # Time: O(n^2)  Space: O(n)
# @lc code=end
