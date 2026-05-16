#
# @lc app=leetcode id=1011 lang=python
#
# [1011] Capacity To Ship Packages Within D Days
#
# PROBLEM:
# Packages must be shipped in order. The conveyor belt has capacity units/day.
# Return the minimum weight capacity needed to ship all packages within d days.
# Example: weights=[1,2,3,4,5,6,7,8,9,10], days=5 → 15
#
# APPROACH: Binary search on answer (capacity).
# - Lower bound: max(weights) — must fit heaviest package in one day
# - Upper bound: sum(weights) — ship everything in one day
# For a given capacity, greedily check if it fits in <= d days.

# @lc code=start
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def can_ship(capacity):
            required_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    required_days += 1
                    current_load = 0
                current_load += w
            return required_days <= days

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
        # Time: O(n log(sum-max))  Space: O(1)
# @lc code=end
