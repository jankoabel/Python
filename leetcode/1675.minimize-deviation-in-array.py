#
# @lc app=leetcode id=1675 lang=python
#
# [1675] Minimize Deviation in Array (HARD)
#
# PROBLEM:
# Given an array nums, perform operations:
# - If num is even: divide by 2
# - If num is odd: multiply by 2
# Minimize max(nums) - min(nums).
# Example: nums=[1,2,3,4] → 1
#
# APPROACH: Normalize all to even (multiply all odds by 2).
# Use a max-heap. Always divide the maximum. Track minimum.
# Stop when max is odd (can't divide further).

# @lc code=start
import heapq

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []  # max-heap (negate)
        min_val = float('inf')

        for num in nums:
            if num % 2 == 1:
                num *= 2  # make all even
            heapq.heappush(heap, -num)
            min_val = min(min_val, num)

        result = float('inf')

        while True:
            max_val = -heapq.heappop(heap)
            result = min(result, max_val - min_val)
            if max_val % 2 == 1:
                break  # can't divide an odd number → stop
            half = max_val // 2
            min_val = min(min_val, half)
            heapq.heappush(heap, -half)

        return result
        # Time: O(n log n log(max_val))  Space: O(n)
# @lc code=end
