#
# @lc app=leetcode id=1074 lang=python
#
# [1074] Number of Submatrices That Sum to Target (HARD)
#
# PROBLEM:
# Given a matrix and target, return the number of non-empty submatrices
# that sum to target.
# Example: matrix=[[0,1,0],[1,1,1],[0,1,0]], target=0 → 4
#
# APPROACH: Fix top and bottom rows. For each column pair, compute column sums.
# Then use prefix sum + hashmap (like "Subarray Sum Equals K") on the row sums.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        count = 0

        for r1 in range(m):
            col_sum = [0] * n
            for r2 in range(r1, m):
                for c in range(n):
                    col_sum[c] += matrix[r2][c]

                # Now find subarrays of col_sum that equal target
                prefix_count = defaultdict(int)
                prefix_count[0] = 1
                prefix = 0
                for s in col_sum:
                    prefix += s
                    count += prefix_count[prefix - target]
                    prefix_count[prefix] += 1

        return count
        # Time: O(m^2 * n)  Space: O(n)
# @lc code=end
