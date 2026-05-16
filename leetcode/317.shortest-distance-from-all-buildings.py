#
# @lc app=leetcode id=317 lang=python
#
# [317] Shortest Distance from All Buildings (HARD)
#
# PROBLEM:
# In a grid: 0=empty, 1=building, 2=obstacle. Find the empty cell with
# minimum total distance to all buildings. Return -1 if none.
# Example: grid=[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]] → 7
#
# APPROACH: BFS from each building to compute distances to all reachable empty cells.
# Accumulate total_dist and reachability_count. Answer = min total_dist where
# count == number of buildings.

# @lc code=start
from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        total_dist = [[0] * n for _ in range(m)]
        reachable  = [[0] * n for _ in range(m)]
        buildings  = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    buildings += 1
                    # BFS from this building
                    visited = [[False]*n for _ in range(m)]
                    queue = deque([(r, c, 0)])
                    visited[r][c] = True
                    while queue:
                        cr, cc, dist = queue.popleft()
                        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                            nr, nc = cr+dr, cc+dc
                            if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]==0:
                                visited[nr][nc] = True
                                total_dist[nr][nc] += dist + 1
                                reachable[nr][nc]  += 1
                                queue.append((nr, nc, dist+1))

        result = float('inf')
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and reachable[r][c] == buildings:
                    result = min(result, total_dist[r][c])

        return result if result != float('inf') else -1
        # Time: O(m^2 * n^2)  Space: O(m*n)
# @lc code=end
