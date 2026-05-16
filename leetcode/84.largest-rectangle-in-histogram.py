#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Monotonic stack: maintain a stack of bars in increasing height order
        # When we see a shorter bar, we know all taller bars on the stack
        # cannot extend further right → calculate their area now
        stack = []   # stores (index, height) — index = where this bar "started"
        max_area = 0

        for i, h in enumerate(heights):
            start = i  # the leftmost index this bar can extend to
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # This bar spans from idx to i-1 (width = i - idx)
                max_area = max(max_area, height * (i - idx))
                start = idx   # current bar can extend back to where the taller bar started
            stack.append((start, h))

        # Process remaining bars in stack — they extend to the end
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))

        return max_area
        # Time: O(n)  Space: O(n)
# @lc code=end
