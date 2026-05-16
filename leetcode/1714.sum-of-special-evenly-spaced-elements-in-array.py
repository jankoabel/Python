#
# @lc app=leetcode id=1714 lang=python
#
# [1714] Sum Of Special Evenly-Spaced Elements In Array (HARD)
#
# PROBLEM:
# Given nums (0-indexed) and queries[i]=[xi, yi], for each query return
# sum of nums[xi], nums[xi+yi], nums[xi+2*yi], ... modulo 10^9+7.
# Example: nums=[0,1,2,3,4,5,6,7], queries=[[0,3],[5,1],[4,2]] → [9,18,10]
#
# APPROACH: Square root decomposition.
# For small yi (<= sqrt(n)): precompute suffix sums with given step.
# For large yi (> sqrt(n)): direct computation (at most sqrt(n) terms).

# @lc code=start
class Solution(object):
    def solve(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(nums)
        B = max(1, int(n**0.5))

        # Precompute for small steps: dp[step][i] = sum from i with step
        dp = {}
        for step in range(1, B + 1):
            suffix = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                suffix[i] = (nums[i] + (suffix[i + step] if i + step < n else 0)) % MOD
            dp[step] = suffix

        result = []
        for x, y in queries:
            if y <= B:
                result.append(dp[y][x])
            else:
                s = 0
                i = x
                while i < n:
                    s = (s + nums[i]) % MOD
                    i += y
                result.append(s)

        return result
        # Time: O(n*sqrt(n) + q*sqrt(n))  Space: O(n*sqrt(n))
# @lc code=end
