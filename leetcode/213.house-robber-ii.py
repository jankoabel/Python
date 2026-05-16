#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_range(houses):
            prev2, prev1 = 0, 0
            for num in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1
        if len(nums) == 1:
            return nums[0]
        return max(rob_range(nums[:-1]), rob_range(nums[1:]))
# @lc code=end
