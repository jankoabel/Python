#
# @lc app=leetcode id=1000 lang=python
#
# [1000] Minimum Cost to Merge Stones (HARD)
#
# PROBLEM:
# There are n piles of stones. Merge exactly k consecutive piles into one pile
# (cost = sum of piles merged). Return minimum cost to merge all into one pile.
# Return -1 if impossible.
# Example: stones=[3,2,4,1], k=2 → 20
#
# APPROACH: Interval DP with prefix sums.
# dp[i][j] = min cost to reduce stones[i..j] to minimum possible piles.
# A range of length L can be reduced to 1 pile iff (L-1) % (k-1) == 0.
# Otherwise it reduces to ((L-1) % (k-1)) + 1 piles.

# @lc code=start
class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i, s in enumerate(stones):
            prefix[i+1] = prefix[i] + s

        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j])
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j+1] - prefix[i]

        return dp[0][n-1]
        # Time: O(n^3 / k)  Space: O(n^2)
# @lc code=end
