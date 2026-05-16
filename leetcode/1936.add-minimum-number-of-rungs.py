#
# @lc app=leetcode id=1936 lang=python
#
# [1936] Add Minimum Number of Rungs
#
# PROBLEM:
# A ladder has rungs at certain heights. You can climb at most 'dist' at each step.
# Return minimum rungs to add so you can reach the top.
# Example: rungs=[1,3,5,10], dist=2 → 2 (add between 5 and 10)
#
# APPROACH: Greedy. For each gap between consecutive rungs (including from 0),
# if gap > dist, you need ceil(gap/dist) - 1 new rungs.

# @lc code=start
import math

class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        count = 0
        prev = 0
        for rung in rungs:
            gap = rung - prev
            if gap > dist:
                count += math.ceil(gap / dist) - 1
            prev = rung
        return count
        # Time: O(n)  Space: O(1)
# @lc code=end
