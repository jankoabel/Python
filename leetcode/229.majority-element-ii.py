#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#
# PROBLEM:
# Given an integer array, return all elements that appear more than n/3 times.
# There can be at most 2 such elements. Must run in O(n) time and O(1) space.
# Example: [3,2,3] → [3]  ;  [1,2] → [1,2]
#
# APPROACH: Extended Boyer-Moore voting with 2 candidates.
# Track two candidates and their counts. Cancel triplets (1 of each + 1 other).
# Final pass to verify counts (candidates may not actually be majority).

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c1, c2 = None, None   # candidates
        cnt1, cnt2 = 0, 0     # counts

        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1
            elif cnt1 == 0:
                c1, cnt1 = num, 1     # new candidate 1
            elif cnt2 == 0:
                c2, cnt2 = num, 1     # new candidate 2
            else:
                cnt1 -= 1    # cancel triplet
                cnt2 -= 1

        # Verify candidates actually appear more than n/3 times
        n = len(nums)
        return [c for c in (c1, c2) if c is not None and nums.count(c) > n // 3]
        # Time: O(n)  Space: O(1)
# @lc code=end
