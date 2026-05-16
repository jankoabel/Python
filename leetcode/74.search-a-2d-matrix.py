#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Treat the m x n matrix as a flat sorted array of size m*n
        # Binary search on index [0, m*n - 1]
        # Map flat index i → row = i // n, col = i % n
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // cols][mid % cols]   # convert flat index to 2D

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        # Time: O(log(m*n))  Space: O(1)
# @lc code=end
