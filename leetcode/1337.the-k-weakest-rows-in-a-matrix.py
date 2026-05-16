#
# @lc app=leetcode id=1337 lang=python
#
# [1337] The K Weakest Rows in a Matrix
#
# PROBLEM:
# Given a binary matrix where soldiers (1s) always precede civilians (0s) in each row,
# return the indices of the k weakest rows (fewest soldiers), breaking ties by row index.
# Example: mat=[[1,1,0],[1,1,1],[1,0,0],[1,1,0],[1,1,1]], k=3 → [2,0,3]
#
# APPROACH: Binary search to count soldiers per row (since 1s precede 0s).
# Sort rows by (soldier_count, row_index), take first k.

# @lc code=start
import bisect

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def soldier_count(row):
            # Binary search for first 0 — count of 1s equals that index
            return bisect.bisect_right(row, 1) - bisect.bisect_left(row, 1) + bisect.bisect_right(row, 1)

        # Simpler: since row is sorted 1s then 0s, sum gives count directly
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        strengths.sort()
        return [i for _, i in strengths[:k]]
        # Time: O(m*n + m log m)  Space: O(m)
# @lc code=end
