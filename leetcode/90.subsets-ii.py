#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Same as Subsets but with duplicates — sort first, then skip duplicate
        # choices at the same recursion level to avoid identical subsets
        nums.sort()
        result = []

        def backtrack(start, current):
            result.append(list(current))

            for i in range(start, len(nums)):
                # Skip duplicate elements at the same level of recursion
                # (only skip if it's NOT the first pick at this level)
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result
        # Time: O(2^n * n)  Space: O(n)
# @lc code=end
