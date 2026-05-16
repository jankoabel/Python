#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Backtracking: at each step, pick an unused number and recurse
        result = []

        def backtrack(current, remaining):
            if not remaining:               # used all numbers — complete permutation
                result.append(list(current))
                return
            for i in range(len(remaining)):
                current.append(remaining[i])
                # remaining without the chosen element
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()               # undo choice

        backtrack([], nums)
        return result
        # Time: O(n! * n)  Space: O(n)
# @lc code=end
