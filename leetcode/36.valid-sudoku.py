#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#
# PROBLEM:
# Determine if a 9x9 Sudoku board is valid. Only filled cells need validation.
# Rules: each row, each column, each 3x3 box must contain digits 1-9 without repetition.
#
# APPROACH: Track seen numbers in rows, cols, and 3x3 boxes using sets.
# Box index = (row//3, col//3)

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]   # 3x3 boxes indexed 0-8

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue   # empty cell, skip

                box_idx = (r // 3) * 3 + (c // 3)   # which of the 9 boxes

                # Check for duplicates in row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True
        # Time: O(81) = O(1)  Space: O(81) = O(1)
# @lc code=end
