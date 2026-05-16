#
# @lc app=leetcode id=1431 lang=python
#
# [1431] Kids With the Greatest Number of Candies
#
# PROBLEM:
# Given candies[] and extraCandies, for each kid return True if they can have
# the greatest number of candies (after giving them all extraCandies).
# Example: candies=[2,3,5,1,3], extraCandies=3 → [True,True,True,False,True]
#
# APPROACH: Find the current max. Kid i qualifies if candies[i] + extraCandies >= max.

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
        # Time: O(n)  Space: O(n)
# @lc code=end
