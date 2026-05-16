#
# @lc app=leetcode id=407 lang=python
#
# [407] Trapping Rain Water II (HARD)
#
# PROBLEM:
# Given an m×n grid of heights, return the volume of water it can trap after raining.
# Example: heightMap=[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] → 4
#
# APPROACH: Min-heap (priority queue).
# Start with all border cells. Greedily process the lowest border cell.
# Water level inside is bounded by the minimum border height.
# For each neighbor: if lower than current level, it traps water.

# @lc code=start
import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or len(heightMap) < 3:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        heap = []

        # Push all border cells
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m-1 or c == 0 or c == n-1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water = 0
        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water += max(0, h - heightMap[nr][nc])
                    heapq.heappush(heap, (max(h, heightMap[nr][nc]), nr, nc))

        return water
        # Time: O(m*n log(m*n))  Space: O(m*n)
# @lc code=end
