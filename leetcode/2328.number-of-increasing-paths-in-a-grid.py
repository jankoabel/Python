#
# @lc app=leetcode id=2328 lang=python
#
# [2328] Number of Increasing Paths in a Grid (HARD)
#
# PROBLEM:
# Find the number of strictly increasing paths in a grid (move 4-directionally).
# Return count modulo 10^9+7.
# Example: grid=[[1,1],[3,4]] → 8
#
# APPROACH: DFS + memoization. Sort cells by value and process in order.
# dp[r][c] = number of increasing paths starting at (r,c).

# @lc code=start
from functools import lru_cache

class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dp(r, c):
            count = 1  # path of length 1 (just this cell)
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] > grid[r][c]:
                    count += dp(nr, nc)
            return count % MOD

        return sum(dp(r, c) for r in range(m) for c in range(n)) % MOD
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
