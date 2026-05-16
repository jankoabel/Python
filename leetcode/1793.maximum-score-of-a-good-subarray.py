#
# @lc app=leetcode id=1793 lang=python
#
# [1793] Maximum Score of a Good Subarray (HARD)
#
# PROBLEM:
# Score of subarray [i, j] = min(nums[i..j]) * (j - i + 1).
# A good subarray includes index k (i <= k <= j).
# Return max score.
# Example: nums=[1,4,3,7,4,5], k=3 → 15 (subarray [3,5]: min=4, len=3 → 12? or [1,5]: min=1*6=6)
#
# APPROACH: Two pointers from k outward, always expanding toward the larger neighbor.
# Track minimum as we expand.

# @lc code=start
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        lo = hi = k
        min_val = nums[k]
        result = min_val

        while lo > 0 or hi < n - 1:
            # Expand toward the larger side to delay reducing min
            if lo == 0:
                hi += 1
            elif hi == n - 1:
                lo -= 1
            elif nums[lo - 1] >= nums[hi + 1]:
                lo -= 1
            else:
                hi += 1

            min_val = min(min_val, nums[lo], nums[hi])
            result = max(result, min_val * (hi - lo + 1))

        return result
        # Time: O(n)  Space: O(1)
# @lc code=end
