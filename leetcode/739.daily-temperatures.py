#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#
# PROBLEM:
# Given an array of temperatures, for each day find how many days you have to wait
# until a warmer temperature. If no future warmer day exists, return 0 for that day.
# Example: temperatures=[73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
#
# APPROACH: Monotonic stack (decreasing).
# Push indices. When we find a warmer temperature, resolve all stack entries
# that are cooler. Result[i] = current_index - stacked_index.

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n
        stack = []  # indices, monotonic decreasing by temperature

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                result[j] = i - j   # days to wait
            stack.append(i)

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
