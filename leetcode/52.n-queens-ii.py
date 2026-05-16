#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II (HARD)
#
# PROBLEM:
# Return the number of distinct solutions to the N-Queens puzzle.
# Example: n=4 → 2  ;  n=1 → 1
#
# APPROACH: Backtracking — same as N-Queens but only count solutions.
# Track used columns, diagonals (\), and anti-diagonals (/).

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        cols  = set()
        diag1 = set()  # row - col (\ diagonals)
        diag2 = set()  # row + col (/ anti-diagonals)

        def backtrack(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                cols.add(col); diag1.add(row-col); diag2.add(row+col)
                backtrack(row + 1)
                cols.discard(col); diag1.discard(row-col); diag2.discard(row+col)

        backtrack(0)
        return self.count
        # Time: O(n!)  Space: O(n)
# @lc code=end
