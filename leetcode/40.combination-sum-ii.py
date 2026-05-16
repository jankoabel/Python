#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Each number can only be used ONCE, and candidates may have duplicates
        # Sort first, then skip duplicates at the same recursion level
        candidates.sort()
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break   # sorted → all further elements are too large
                # Skip duplicate elements at the same level (not deeper levels)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, current, remaining - candidates[i])   # i+1: no reuse
                current.pop()

        backtrack(0, [], target)
        return result
        # Time: O(2^n)  Space: O(n)
# @lc code=end
