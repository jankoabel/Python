#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
# PROBLEM:
# Given a triangle array, find the minimum path sum from top to bottom.
# At each step you may move to an adjacent number in the row below
# (index i → index i or i+1 in next row).
# Example: [[2],[3,4],[6,5,7],[4,1,8,3]] → 11 (2→3→5→1)
#
# APPROACH: Bottom-up DP. Start from second-to-last row, working up.
# dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Start with a copy of the last row
        dp = list(triangle[-1])

        # Work upward from second-to-last row
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Best path from (i,j) = triangle[i][j] + min of two paths below
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]   # top of triangle
        # Time: O(n^2)  Space: O(n)
# @lc code=end
