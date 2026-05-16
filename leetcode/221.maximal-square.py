#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#
# PROBLEM:
# Given an m x n binary matrix, find the largest square containing only 1s
# and return its area.
# Example: [["1","0","1","0","0"],
#            ["1","0","1","1","1"],
#            ["1","1","1","1","1"],
#            ["1","0","0","1","0"]] → 4
#
# APPROACH: DP. dp[i][j] = side length of largest square with (i,j) as bottom-right corner.
# If matrix[i][j] == '1':
#   dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# Intuition: limited by the smallest of the three neighboring squares.

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]   # +1 padding avoids edge cases
        max_side = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side   # area = side^2
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
