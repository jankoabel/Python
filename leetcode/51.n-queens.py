#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens (HARD)
#
# PROBLEM:
# Place n queens on an n×n chessboard so no two queens attack each other.
# Queens attack along rows, columns, and diagonals.
# Return all distinct solutions (each solution is a board configuration).
#
# APPROACH: Backtracking row by row.
# Track which columns, diagonals, and anti-diagonals are occupied.
# Diagonal key: row - col (same for all cells on same diagonal)
# Anti-diagonal key: row + col

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        queens = []   # queens[r] = column of queen placed in row r

        cols = set()
        diag = set()       # row - col
        anti_diag = set()  # row + col

        def backtrack(row):
            if row == n:
                # Build board from queen positions
                board = []
                for r in range(n):
                    board.append('.' * queens[r] + 'Q' + '.' * (n - queens[r] - 1))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in anti_diag:
                    continue    # this cell is under attack

                # Place queen
                queens.append(col)
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)

                backtrack(row + 1)

                # Remove queen (backtrack)
                queens.pop()
                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)

        backtrack(0)
        return result
        # Time: O(n!)  Space: O(n)
# @lc code=end
