#
# @lc app=leetcode id=2218 lang=python
#
# [2218] Maximum Value of K Coins From Piles (HARD)
#
# PROBLEM:
# There are n piles of coins. Each turn, pick the top coin from any pile.
# Pick exactly k coins total. Return maximum sum.
# Example: piles=[[1,100,3],[7,8,9]], k=2 → 101
#
# APPROACH: 2D DP (knapsack style).
# dp[i][j] = max sum using j coins from first i piles.
# For each pile i, try taking 0..min(pile_size, j) coins from pile i.

# @lc code=start
class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :rtype: int
        """
        dp = [0] * (k + 1)  # dp[j] = max sum using j coins from piles so far

        for pile in piles:
            # Prefix sums of this pile for quick range sum queries
            prefix = [0]
            for coin in pile:
                prefix.append(prefix[-1] + coin)

            # Update dp right-to-left (0/1 knapsack style)
            for j in range(k, 0, -1):
                for take in range(1, min(len(pile), j) + 1):
                    dp[j] = max(dp[j], dp[j - take] + prefix[take])

        return dp[k]
        # Time: O(k * sum_of_pile_sizes)  Space: O(k)
# @lc code=end
