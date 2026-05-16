#
# @lc app=leetcode id=1926 lang=python
#
# [1926] Nearest Exit from Entrance in Maze
#
# PROBLEM:
# Given a maze ('.' = empty, '+' = wall) and an entrance cell,
# return minimum steps to reach any boundary cell that is not the entrance.
# Return -1 if impossible.
# Example: maze=[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance=[1,2] → 1
#
# APPROACH: BFS from entrance. Stop when we reach a boundary cell (not entrance).

# @lc code=start
from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        er, ec = entrance

        def is_exit(r, c):
            return (r == 0 or r == m-1 or c == 0 or c == n-1) and (r, c) != (er, ec)

        queue = deque([(er, ec, 0)])
        maze[er][ec] = '+'  # mark visited

        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    if is_exit(nr, nc):
                        return steps + 1
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))

        return -1
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
