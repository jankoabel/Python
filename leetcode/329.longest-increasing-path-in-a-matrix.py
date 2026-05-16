#
# @lc app=leetcode id=329 lang=python
#
# [329] Longest Increasing Path in a Matrix (HARD)
#
# PROBLEM:
# Given an m x n integers matrix, find the length of the longest increasing path.
# From each cell, you can move in 4 directions. You CANNOT move diagonally or outside.
# Each step must be to a strictly greater value.
# Example: [[9,9,4],[6,6,8],[2,1,1]] → 4 (path: 1→2→6→9)
#
# APPROACH: DFS + memoization (top-down DP).
# memo[r][c] = length of longest increasing path starting at (r,c).
# Since path must be strictly increasing, no cycle possible → safe to memoize.

# @lc code=start
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            best = 1   # minimum path length from here is 1 (just this cell)
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    # Only go to strictly larger neighbors
                    best = max(best, 1 + dfs(nr, nc))

            memo[(r, c)] = best
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
