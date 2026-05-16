#
# @lc app=leetcode id=2352 lang=python
#
# [2352] Equal Row and Column Pairs
#
# PROBLEM:
# Given an n×n matrix, return the number of pairs (ri, cj) where row ri
# equals column cj (as sequences).
# Example: grid=[[3,2,1],[1,7,6],[2,7,7]] → 1
#
# APPROACH: Store all rows as tuples in a Counter.
# For each column (as a tuple), look up how many rows match it.

# @lc code=start
from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_counts = Counter(tuple(row) for row in grid)
        count = 0
        n = len(grid)
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            count += row_counts[col]
        return count
        # Time: O(n^2)  Space: O(n^2)
# @lc code=end
