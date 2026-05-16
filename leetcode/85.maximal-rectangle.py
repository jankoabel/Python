#
# @lc app=leetcode id=85 lang=python
#
# [85] Maximal Rectangle (HARD)
#
# PROBLEM:
# Given a binary matrix filled with 0s and 1s, find the largest rectangle
# containing only 1s and return its area.
# Example: [["1","0","1","0","0"],
#            ["1","0","1","1","1"],
#            ["1","1","1","1","1"],
#            ["1","0","0","1","0"]] → 6
#
# APPROACH: Extend Largest Rectangle in Histogram to 2D.
# Build a "height" array for each row:
#   heights[col] += 1 if matrix[row][col] == '1', else reset to 0
# Then apply the histogram algorithm on each row's heights.

# @lc code=start
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largest_in_histogram(heights):
            stack = []   # (start_index, height)
            max_a = 0
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    max_a = max(max_a, height * (i - idx))
                    start = idx
                stack.append((start, h))
            for idx, height in stack:
                max_a = max(max_a, height * (len(heights) - idx))
            return max_a

        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == '1' else 0  # extend or reset

            max_area = max(max_area, largest_in_histogram(heights))

        return max_area
        # Time: O(rows * cols)  Space: O(cols)
# @lc code=end
