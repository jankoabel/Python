#
# @lc app=leetcode id=2104 lang=python
#
# [2104] Sum of Subarray Ranges
#
# PROBLEM:
# The range of a subarray = max(subarray) - min(subarray).
# Return sum of ranges of all subarrays of nums.
# Example: nums=[1,2,3] → 4
#
# APPROACH: Contribution technique with monotonic stacks.
# Sum of max of all subarrays - sum of min of all subarrays.
# For each element, find how many subarrays it is the max/min of.

# @lc code=start
class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def sum_of_extremes(is_max):
            total = 0
            stack = []
            for i, v in enumerate(nums + [float('inf') if is_max else float('-inf')]):
                while stack and (nums[stack[-1]] < v if is_max else nums[stack[-1]] > v):
                    mid = stack.pop()
                    left = stack[-1] if stack else -1
                    right = i
                    count = (mid - left) * (right - mid)
                    total += nums[mid] * count
                stack.append(i)
            return total

        return sum_of_extremes(True) - sum_of_extremes(False)
        # Time: O(n)  Space: O(n)
# @lc code=end
