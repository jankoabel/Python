#
# @lc app=leetcode id=174 lang=python
#
# [174] Dungeon Game (HARD)
#
# PROBLEM:
# Knight starts top-left of a dungeon grid. Must reach bottom-right.
# Each cell has an integer (positive = health gained, negative = health lost).
# Knight dies if health drops to 0 or below at any point.
# Return minimum initial health needed.
# Example: dungeon=[[-2,-3,3],[-5,-10,1],[10,30,-5]] → 7
#
# APPROACH: DP from bottom-right to top-left.
# dp[i][j] = minimum health needed when entering cell (i,j).
# dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
# (Must have at least 1 health; subtract current cell value from needed health)

# @lc code=start
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        # Fill with high value (out-of-bounds acts as infinity)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = dp[m-1][n] = 1  # boundary: need at least 1 health

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_needed = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, min_needed)

        return dp[0][0]
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
