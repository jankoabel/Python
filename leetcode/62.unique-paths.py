#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for _ in range(m - 1):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]
# @lc code=end
