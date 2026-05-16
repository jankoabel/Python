#
# @lc app=leetcode id=2163 lang=python
#
# [2163] Minimum Difference in Sums After Removal of Elements (HARD)
#
# PROBLEM:
# Array of 3n elements. Remove n elements from front, n from back (exact n each).
# Minimize sum(first part) - sum(second part).
# Example: nums=[3,1,2] → -1
#
# APPROACH:
# prefix_min[i] = min sum of n elements from nums[0..i] (using max-heap to keep smallest n)
# suffix_max[i] = max sum of n elements from nums[i..3n-1] (using min-heap to keep largest n)
# Answer = min over split point i of prefix_min[i] - suffix_max[i+1]

# @lc code=start
import heapq

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 3
        total = len(nums)

        # Compute prefix sums: min sum of n elements for each prefix ending at i
        prefix = [0] * total
        heap = []  # max-heap (negate)
        s = 0
        for i in range(total):
            heapq.heappush(heap, -nums[i])
            s += nums[i]
            if len(heap) > n:
                s += heapq.heappop(heap)  # remove largest (most negative neg)
            if len(heap) == n:
                prefix[i] = s

        # Compute suffix sums: max sum of n elements for each suffix starting at i
        suffix = [0] * total
        heap2 = []  # min-heap
        s = 0
        for i in range(total - 1, -1, -1):
            heapq.heappush(heap2, nums[i])
            s += nums[i]
            if len(heap2) > n:
                s -= heapq.heappop(heap2)
            if len(heap2) == n:
                suffix[i] = s

        return min(prefix[i] - suffix[i+1] for i in range(n-1, 2*n))
        # Time: O(n log n)  Space: O(n)
# @lc code=end
