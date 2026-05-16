#
# @lc app=leetcode id=1207 lang=python
#
# [1207] Unique Number of Occurrences
#
# PROBLEM:
# Given an array arr, return true if the number of occurrences of each value
# is unique.
# Example: arr=[1,2,2,1,1,3] → True (1 appears 3, 2 appears 2, 3 appears 1 — all unique)
#
# APPROACH: Count frequencies with a Counter, then check if the count values
# are all distinct by comparing set size.

# @lc code=start
from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = Counter(arr)
        # All occurrence counts must be distinct
        return len(counts) == len(set(counts.values()))
        # Time: O(n)  Space: O(n)
# @lc code=end
