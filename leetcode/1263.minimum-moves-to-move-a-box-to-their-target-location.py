#
# @lc app=leetcode id=1263 lang=python
#
# [1263] Minimum Moves to Move a Box to Their Target Location (HARD)
#
# PROBLEM:
# Grid has '#' (walls), '.' (empty), 'B' (box), 'S' (storekeeper), 'T' (target).
# Push the box to T with minimum pushes. The storekeeper must be able to reach
# the push position. Return minimum pushes or -1.
#
# APPROACH: Dijkstra-like BFS with state (box_pos, player_pos).
# Cost = number of pushes (each push costs 1).
# Player movement between pushes is free (use BFS to check reachability).

# @lc code=start
from collections import deque
import heapq

class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'B': box = (r, c)
                elif grid[r][c] == 'S': player = (r, c)
                elif grid[r][c] == 'T': target = (r, c)

        def can_reach(start, goal, box_pos):
            if start == goal: return True
            visited = set([start])
            queue = deque([start])
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]!='#' \
                       and (nr,nc)!=box_pos and (nr,nc) not in visited:
                        if (nr,nc) == goal: return True
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return False

        heap = [(0, box, player)]
        visited = set()

        while heap:
            pushes, box_pos, p_pos = heapq.heappop(heap)
            if box_pos == target:
                return pushes
            if (box_pos, p_pos) in visited:
                continue
            visited.add((box_pos, p_pos))

            br, bc = box_pos
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                # To push box in direction (dr,dc), player must be at (br-dr, bc-dc)
                push_from = (br - dr, bc - dc)
                new_box   = (br + dr, bc + dc)
                if 0<=new_box[0]<m and 0<=new_box[1]<n and grid[new_box[0]][new_box[1]]!='#':
                    if can_reach(p_pos, push_from, box_pos):
                        heapq.heappush(heap, (pushes+1, new_box, box_pos))

        return -1
        # Time: O((m*n)^2 * log(m*n))  Space: O((m*n)^2)
# @lc code=end
