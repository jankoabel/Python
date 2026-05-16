#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DFS flood fill — same idea as Number of Islands
        # but count the size of each island instead of just incrementing a counter
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            # Out of bounds or water → area contribution is 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0    # mark as visited (sink the island cell)
            # This cell (1) + all connected land cells
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
        # Time: O(rows * cols)  Space: O(rows * cols) call stack
# @lc code=end
