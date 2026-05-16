#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Unbounded knapsack — count combinations (ORDER DOESN'T MATTER)
        # dp[a] = number of ways to make amount a
        # Process each coin type fully before moving to the next
        # (this ensures we count combinations, not permutations)
        dp = [0] * (amount + 1)
        dp[0] = 1   # one way to make amount 0: use no coins

        for coin in coins:
            for a in range(coin, amount + 1):
                # Using this coin: ways to make (a - coin) → now add coin to make a
                dp[a] += dp[a - coin]

        return dp[amount]
        # Time: O(amount * len(coins))  Space: O(amount)
# @lc code=end
