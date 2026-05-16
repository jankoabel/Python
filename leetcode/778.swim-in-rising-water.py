#
# @lc app=leetcode id=778 lang=python
#
# [778] Swim in Rising Water (HARD)
#
# PROBLEM:
# Grid[i][j] is the elevation at (i,j). You can move to 4-adjacent cells.
# At time t, you can swim anywhere the elevation is <= t.
# Return minimum t to swim from (0,0) to (n-1,n-1).
# Example: grid=[[0,2],[1,3]] → 3
#
# APPROACH: Dijkstra / Binary search + BFS.
# Treat as shortest path where edge cost = max elevation along path.
# Use min-heap: (max_elevation_so_far, row, col).

# @lc code=start
import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return t
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

        return -1
        # Time: O(n^2 log n)  Space: O(n^2)
# @lc code=end
