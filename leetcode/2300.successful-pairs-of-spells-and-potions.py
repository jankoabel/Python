#
# @lc app=leetcode id=2300 lang=python
#
# [2300] Successful Pairs of Spells and Potions
#
# PROBLEM:
# Given spells[] and potions[], a pair (spell, potion) is successful if
# spell * potion >= success. Return for each spell the number of successful potions.
# Example: spells=[5,1,3], potions=[1,2,3,4,5], success=7 → [4,0,3]
#
# APPROACH: Sort potions. For each spell, binary search for the minimum potion
# that satisfies spell * potion >= success → min_potion = ceil(success/spell).

# @lc code=start
import bisect
import math

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        result = []
        n = len(potions)
        for spell in spells:
            min_potion = math.ceil(success / float(spell))
            # Binary search for first potion >= min_potion
            idx = bisect.bisect_left(potions, min_potion)
            result.append(n - idx)
        return result
        # Time: O((m+n) log n)  Space: O(1)
# @lc code=end
