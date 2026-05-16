#
# @lc app=leetcode id=2366 lang=python
#
# [2366] Minimum Replacements to Sort the Array (HARD)
#
# PROBLEM:
# Replace any element with 2 or more elements summing to it.
# Return minimum number of replacements to make array non-decreasing.
# Example: nums=[3,9,3] → 2  ;  nums=[1,2,3,4,5] → 0
#
# APPROACH: Greedy from right to left.
# Last element is always fine. For each element from right to left:
# If nums[i] <= nums[i+1]: ok, update limit to nums[i].
# Else: need to split nums[i] into parts <= nums[i+1].
# Operations = ceil(nums[i] / nums[i+1]) - 1.
# New effective value = nums[i] // parts (to be as large as possible for left neighbors).

# @lc code=start
import math

class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ops = 0
        limit = nums[-1]

        for i in range(n - 2, -1, -1):
            if nums[i] <= limit:
                limit = nums[i]
            else:
                parts = math.ceil(nums[i] / limit)
                ops += parts - 1
                limit = nums[i] // parts  # leftmost part (smallest)

        return ops
        # Time: O(n)  Space: O(1)
# @lc code=end
