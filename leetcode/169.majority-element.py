#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
# PROBLEM:
# Given an array of size n, return the majority element (appears more than n/2 times).
# The majority element always exists. Must run in O(n) time and O(1) space.
# Example: [3,2,3] → 3  ;  [2,2,1,1,1,2,2] → 2
#
# APPROACH: Boyer-Moore Voting Algorithm.
# Maintain a candidate and a count.
# Count = 0 → new candidate.
# Same as candidate → count++.
# Different → count-- (cancel one majority with one minority vote).
# The majority element will always survive the cancellations.

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num   # no current candidate, pick this one
            count += 1 if num == candidate else -1   # vote for or against

        return candidate   # guaranteed to be the majority element
        # Time: O(n)  Space: O(1)
# @lc code=end
