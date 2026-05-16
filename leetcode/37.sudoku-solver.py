#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver (HARD)
#
# PROBLEM:
# Solve a Sudoku puzzle by filling in the empty cells ('.').
# Each row, column, and 3x3 box must contain digits 1-9 without repetition.
#
# APPROACH: Backtracking.
# Find the next empty cell, try digits 1-9, check validity, recurse.
# If a digit leads to no solution, backtrack.

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        """
        rows  = [set() for _ in range(9)]
        cols  = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Pre-populate existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    d = board[r][c]
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[(r//3)*3 + c//3].add(d)

        def backtrack(pos):
            if pos == 81:
                return True
            r, c = divmod(pos, 9)
            if board[r][c] != '.':
                return backtrack(pos + 1)

            box_id = (r//3)*3 + c//3
            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[box_id]:
                    board[r][c] = d
                    rows[r].add(d); cols[c].add(d); boxes[box_id].add(d)
                    if backtrack(pos + 1):
                        return True
                    board[r][c] = '.'
                    rows[r].discard(d); cols[c].discard(d); boxes[box_id].discard(d)

            return False

        backtrack(0)
        # Time: O(9^m) where m=empty cells  Space: O(81)
# @lc code=end
