#
# @lc app=leetcode id=1293 lang=python
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
# PROBLEM:
# Given an m×n grid where 0=empty and 1=obstacle, you can eliminate at most k obstacles.
# Return the minimum steps to reach bottom-right from top-left, or -1 if impossible.
# Example: grid=[[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k=1 → 6
#
# APPROACH: BFS with state (row, col, remaining_eliminations).
# Use a visited set of (row, col, k_remaining) to avoid revisiting worse states.

# @lc code=start
from collections import deque

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        visited = set()
        queue = deque([(0, 0, k, 0)])  # (row, col, k_remaining, steps)
        visited.add((0, 0, k))

        while queue:
            r, c, remaining, steps = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if nr == m - 1 and nc == n - 1:
                        return steps + 1
                    new_k = remaining - grid[nr][nc]
                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        visited.add((nr, nc, new_k))
                        queue.append((nr, nc, new_k, steps + 1))

        return -1
        # Time: O(m*n*k)  Space: O(m*n*k)
# @lc code=end
