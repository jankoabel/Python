#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # If k >= n//2, we can make as many transactions as we want
        # (same as unlimited transactions problem)
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))

        # dp approach: track 'buy' and 'sell' profit for each transaction count
        # buy[j]  = max profit having done j transactions and currently holding stock
        # sell[j] = max profit having completed j transactions (not holding)
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(k, 0, -1):   # process in reverse to avoid using today twice
                # Either keep holding, or buy today (costs price, uses one "slot")
                buy[j] = max(buy[j], sell[j-1] - price)
                # Either keep profit, or sell today
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]
        # Time: O(n * k)  Space: O(k)
# @lc code=end
