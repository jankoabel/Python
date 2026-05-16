#
# @lc app=leetcode id=2444 lang=python
#
# [2444] Count Subarrays With Fixed Bounds (HARD)
#
# PROBLEM:
# Count subarrays where min == minK and max == maxK.
# Example: nums=[1,3,5,2,7,5], minK=1, maxK=5 → 2
#
# APPROACH: One pass.
# Track positions: last_bad (element out of [minK,maxK]), last_min, last_max.
# For each right endpoint, valid subarrays start from (min(last_min,last_max)+1)
# to (last_bad+1). Count = max(0, min(last_min,last_max) - last_bad).

# @lc code=start
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        result = 0
        last_bad = -1  # last index where num < minK or num > maxK
        last_min = -1  # last index where num == minK
        last_max = -1  # last index where num == maxK

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_bad = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            # Number of valid subarrays ending at i
            result += max(0, min(last_min, last_max) - last_bad)

        return result
        # Time: O(n)  Space: O(1)
# @lc code=end
