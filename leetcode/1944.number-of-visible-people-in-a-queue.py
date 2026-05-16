#
# @lc app=leetcode id=1944 lang=python
#
# [1944] Number of Visible People in a Queue (HARD)
#
# PROBLEM:
# People in a queue have heights[]. Person i can see person j (j > i) if all
# people between them are shorter than both heights[i] and heights[j].
# Return count of visible people for each person.
# Example: heights=[10,6,8,5,11,9] → [3,1,2,1,1,0]
#
# APPROACH: Monotonic stack (decreasing) from right to left.
# For each person i, the people they can see = (count popped from stack < heights[i]) + (1 if stack not empty)

# @lc code=start
class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        result = [0] * n
        stack = []  # monotonic decreasing

        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1  # can see the first taller person
            result[i] = count
            stack.append(heights[i])

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
