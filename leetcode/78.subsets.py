#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Backtracking: at each index, choose to INCLUDE or SKIP the element
        # Start with empty subset [], then build up
        result = []

        def backtrack(start, current):
            result.append(list(current))   # every partial state is a valid subset

            for i in range(start, len(nums)):
                current.append(nums[i])    # include nums[i]
                backtrack(i + 1, current)  # recurse on remaining elements
                current.pop()              # exclude nums[i] (backtrack)

        backtrack(0, [])
        return result
        # Time: O(2^n * n)  Space: O(n)
# @lc code=end
