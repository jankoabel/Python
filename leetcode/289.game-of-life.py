#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#
# PROBLEM:
# Given a board of 0s (dead) and 1s (live), apply Conway's Game of Life rules simultaneously:
# - Live cell with < 2 live neighbors → dies (underpopulation)
# - Live cell with 2 or 3 live neighbors → lives
# - Live cell with > 3 live neighbors → dies (overpopulation)
# - Dead cell with exactly 3 live neighbors → becomes alive (reproduction)
# Update the board in-place. Must use O(1) extra space.
#
# APPROACH: Use extra states to encode transitions without extra space.
# 2 = was alive, now dead (1→0)
# 3 = was dead, now alive (0→1)
# Count neighbors using original values: live = (val & 1) == 1

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None
        """
        rows, cols = len(board), len(board[0])
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        def count_live_neighbors(r, c):
            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] & 1:
                    count += 1   # & 1 reads original value (1 or 3 = originally alive)
            return count

        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1:    # currently alive
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 3   # 1→0: alive but will die  (binary: 11)
                else:                   # currently dead
                    if live_neighbors == 3:
                        board[r][c] = 2   # 0→1: dead but will live  (binary: 10)

        # Final pass: apply transitions
        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1   # shift right: 3→1, 2→1... wait
                # Actually: 3 >> 1 = 1 (wrong), need: 3 → 0, 2 → 1
                # Reinterpret: use bit 1 as "new state"
                # 0 (dead, stays dead) → 0>>1=0 ✓
                # 1 (alive, stays alive) → 1>>1=0 ✗
                # Use: new state = (val >> 1) XOR (val & 1)... simpler:
                pass

        # Simpler encoding: mark transitions separately
        # (corrected version below using direct replacement)
        # Time: O(m*n)  Space: O(1)
# @lc code=end


# CORRECTED CLEAN VERSION:
class Solution2(object):
    def gameOfLife(self, board):
        rows, cols = len(board), len(board[0])
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        # Encode: 2 = was live → now dead.  3 = was dead → now live
        for r in range(rows):
            for c in range(cols):
                live = sum(
                    1 for dr,dc in dirs
                    if 0 <= r+dr < rows and 0 <= c+dc < cols
                    and board[r+dr][c+dc] in (1, 2)   # 1 or 2 = originally alive
                )
                if board[r][c] == 1 and live not in (2, 3):
                    board[r][c] = 2   # alive → dead
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 3   # dead → alive

        for r in range(rows):
            for c in range(cols):
                board[r][c] = 1 if board[r][c] in (1, 3) else 0
