#
# @lc app=leetcode id=2009 lang=python
#
# [2009] Minimum Number of Operations to Make Array Continuous (HARD)
#
# PROBLEM:
# An array is continuous if: all elements distinct and max-min == n-1.
# Each operation replaces any element with any integer.
# Return minimum operations to make array continuous.
# Example: nums=[4,2,5,3] → 0  ;  nums=[1,2,3,5,6] → 1
#
# APPROACH: Sort and deduplicate. For each possible left boundary (deduped[i]),
# use binary search to find how many deduped elements fall in [deduped[i], deduped[i]+n-1].
# Those elements are "kept"; the rest are "replaced". Minimize replacements.

# @lc code=start
import bisect

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        deduped = sorted(set(nums))
        best = 0

        for i, left in enumerate(deduped):
            # Count elements in window [left, left+n-1]
            right = left + n - 1
            count = bisect.bisect_right(deduped, right) - i
            best = max(best, count)

        return n - best
        # Time: O(n log n)  Space: O(n)
# @lc code=end
