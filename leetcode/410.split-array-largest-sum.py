#
# @lc app=leetcode id=410 lang=python
#
# [410] Split Array Largest Sum (HARD)
#
# PROBLEM:
# Split array nums into k non-empty subarray(s) to minimize the largest subarray sum.
# Example: nums=[7,2,5,10,8], k=2 → 18 (split [7,2,5] and [10,8])
#
# APPROACH: Binary search on answer.
# - Lower bound: max(nums) — must fit largest element in one subarray
# - Upper bound: sum(nums) — one subarray with everything
# For a given max_sum, greedily check if we can split into <= k subarrays.

# @lc code=start
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def can_split(max_sum):
            parts = 1
            current = 0
            for num in nums:
                if current + num > max_sum:
                    parts += 1
                    current = 0
                current += num
            return parts <= k

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
        # Time: O(n log(sum-max))  Space: O(1)
# @lc code=end
