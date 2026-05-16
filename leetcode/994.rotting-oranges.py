#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Multi-source BFS: start from ALL rotten oranges simultaneously
        # Each BFS level = 1 minute passing
        # After BFS, if any fresh orange remains → return -1
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Seed the queue with all initially rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):   # process one full "wave"
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2     # orange rots
                        fresh -= 1
                        queue.append((nr, nc))

        return minutes if fresh == 0 else -1
        # Time: O(rows * cols)  Space: O(rows * cols)
# @lc code=end
