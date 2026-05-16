#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # DP with a dictionary: dp[sum] = number of ways to reach that sum
        # For each number, we either ADD it or SUBTRACT it
        dp = {0: 1}   # start: one way to reach sum 0 (empty assignment)

        for num in nums:
            next_dp = {}
            for s, count in dp.items():
                # Add num → reach s + num
                next_dp[s + num] = next_dp.get(s + num, 0) + count
                # Subtract num → reach s - num
                next_dp[s - num] = next_dp.get(s - num, 0) + count
            dp = next_dp

        return dp.get(target, 0)
        # Time: O(n * range_of_sums)  Space: O(range_of_sums)
# @lc code=end
