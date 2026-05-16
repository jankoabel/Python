#
# @lc app=leetcode id=334 lang=python
#
# [334] Increasing Triplet Subsequence
#
# PROBLEM:
# Return true if there exist indices i < j < k such that nums[i] < nums[j] < nums[k].
# Must run in O(n) time and O(1) space.
# Example: [1,2,3,4,5] → True  ;  [5,4,3,2,1] → False  ;  [2,1,5,0,4,6] → True
#
# APPROACH: Track first (smallest) and second (second smallest so far).
# If we find something larger than second → triplet found.
# first and second are the "best candidates" to be the first two elements.

# @lc code=start
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num      # update smallest
            elif num <= second:
                second = num     # update second smallest (first < num here)
            else:
                return True      # num > second > first → triplet found!

        return False
        # Time: O(n)  Space: O(1)
# @lc code=end
