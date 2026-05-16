#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#
# PROBLEM:
# Search a matrix where each row is sorted left→right and each column top→bottom.
# Return true if target exists.
# Example: matrix=[[1,4,7],[2,5,8],[3,6,9]], target=5 → True
#
# APPROACH: Start at TOP-RIGHT corner.
# - If current > target → move LEFT (eliminate this column)
# - If current < target → move DOWN (eliminate this row)
# - If equal → found!
# This works because moving left decreases, moving down increases.

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1   # start at top-right

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1    # too large: move left
            else:
                row += 1    # too small: move down

        return False
        # Time: O(m + n)  Space: O(1)
# @lc code=end
