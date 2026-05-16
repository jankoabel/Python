#
# @lc app=leetcode id=312 lang=python
#
# [312] Burst Balloons (HARD)
#
# PROBLEM:
# Given n balloons with values nums[], burst all balloons to maximize coins.
# Bursting balloon i gives nums[i-1]*nums[i]*nums[i+1] coins.
# Example: nums=[3,1,5,8] → 167
#
# APPROACH: Interval DP — think about the LAST balloon to burst in range [i,j].
# dp[i][j] = max coins from bursting all balloons in range (i,j) exclusive.
# Pad nums with 1 on both ends.
# dp[i][j] = max over k in (i+1..j-1) of: dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j]

# @lc code=start
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # l = length of interval
        for l in range(2, n):
            for i in range(0, n - l):
                j = i + l
                for k in range(i + 1, j):
                    # k is the LAST balloon to burst between i and j
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j])

        return dp[0][n-1]
        # Time: O(n^3)  Space: O(n^2)
# @lc code=end
