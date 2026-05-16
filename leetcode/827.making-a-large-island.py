#
# @lc app=leetcode id=827 lang=python
#
# [827] Making A Large Island (HARD)
#
# PROBLEM:
# In a binary grid, flip at most one 0 to 1. Return the size of the largest island.
# Example: grid=[[1,0],[0,1]] → 3
#
# APPROACH:
# 1. Label each island with DFS, record size of each label.
# 2. For each 0, check unique adjacent islands and sum their sizes + 1.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        label = 2  # labels start at 2 to distinguish from 0/1
        island_size = {}

        def dfs(r, c, lbl):
            grid[r][c] = lbl
            size = 1
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 1:
                    size += dfs(nr, nc, lbl)
            return size

        # Label all islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_size[label] = dfs(r, c, label)
                    label += 1

        best = max(island_size.values()) if island_size else 0

        # Try flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    total = 1
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<n and 0<=nc<n and grid[nr][nc] > 1:
                            lbl = grid[nr][nc]
                            if lbl not in seen:
                                seen.add(lbl)
                                total += island_size[lbl]
                    best = max(best, total)

        return best
        # Time: O(n^2)  Space: O(n^2)
# @lc code=end
