#
# @lc app=leetcode id=689 lang=python
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays (HARD)
#
# PROBLEM:
# Given an integer array nums and k, find 3 non-overlapping subarrays of length k
# with maximum sum. Return their starting indices (lexicographically smallest).
# Example: nums=[1,2,1,2,6,7,5,1], k=2 → [0,3,5]
#
# APPROACH: Precompute window sums. Then precompute best left index for each pos,
# and best right index for each pos. Scan middle window and combine.

# @lc code=start
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        # Compute sliding window sums
        sums = [sum(nums[:k])]
        for i in range(k, n):
            sums.append(sums[-1] + nums[i] - nums[i-k])

        # Best window start in sums[0..i]
        left = [0] * n
        best = 0
        for i in range(n):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        # Best window start in sums[i..n-k]
        right = [n - k] * n
        best = n - k
        for i in range(n - k, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        # Scan middle window
        best_sum = 0
        result = [-1, -1, -1]
        for mid in range(k, n - 2*k + 1):
            l, r = left[mid - k], right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if total > best_sum:
                best_sum = total
                result = [l, mid, r]

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
