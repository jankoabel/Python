#
# @lc app=leetcode id=1463 lang=python
#
# [1463] Cherry Pickup II (HARD)
#
# PROBLEM:
# Two robots start at top-left and top-right corners of a grid.
# Each move, both can move to adjacent columns (or stay) on the next row.
# They cannot occupy the same cell. Collect maximum cherries.
# Example: grid=[[3,1,1],[2,5,1],[1,5,5],[2,1,1]] → 24
#
# APPROACH: 3D DP — dp[row][col1][col2].
# At each row, both robots choose their column. If col1==col2, count once.

# @lc code=start
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # dp[c1][c2] = max cherries with robot1 at col c1, robot2 at col c2
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[0][n-1] = grid[0][0] + grid[0][n-1]

        for row in range(1, m):
            new_dp = [[float('-inf')] * n for _ in range(n)]
            for c1 in range(n):
                for c2 in range(n):
                    cherries = grid[row][c1] + (0 if c1 == c2 else grid[row][c2])
                    for dc1 in (-1, 0, 1):
                        for dc2 in (-1, 0, 1):
                            pc1, pc2 = c1 + dc1, c2 + dc2
                            if 0 <= pc1 < n and 0 <= pc2 < n and dp[pc1][pc2] != float('-inf'):
                                new_dp[c1][c2] = max(new_dp[c1][c2], dp[pc1][pc2] + cherries)
            dp = new_dp

        return max(dp[c1][c2] for c1 in range(n) for c2 in range(n))
        # Time: O(m * n^2 * 9)  Space: O(n^2)
# @lc code=end
