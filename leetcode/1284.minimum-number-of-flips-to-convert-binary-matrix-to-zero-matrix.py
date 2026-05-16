#
# @lc app=leetcode id=1284 lang=python
#
# [1284] Minimum Number of Flips to Convert Binary Matrix to Zero Matrix (HARD)
#
# PROBLEM:
# Given a binary matrix, in one flip: flip the cell and its 4-neighbors.
# Return minimum flips to make all zeros, or -1.
# Example: mat=[[0,0],[0,1]] → 3
#
# APPROACH: BFS on bitmask states.
# Encode matrix as bitmask. BFS from initial state to 0.
# Each state transition flips one cell.

# @lc code=start
from collections import deque

class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Encode initial state
        start = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c]:
                    start |= 1 << (r * n + c)

        # Precompute flip masks for each cell
        flip = []
        for r in range(m):
            for c in range(n):
                mask = 1 << (r * n + c)
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n:
                        mask |= 1 << (nr * n + nc)
                flip.append(mask)

        visited = {start}
        queue = deque([(start, 0)])
        while queue:
            state, steps = queue.popleft()
            if state == 0:
                return steps
            for f in flip:
                new_state = state ^ f
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

        return -1
        # Time: O(2^(m*n) * m*n)  Space: O(2^(m*n))
# @lc code=end
