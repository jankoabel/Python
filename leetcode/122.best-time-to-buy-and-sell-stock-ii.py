#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
# PROBLEM:
# You can buy and sell stock as many times as you want
# (but can only hold one stock at a time, and must sell before buying again).
# Find maximum profit.
# Example: [7,1,5,3,6,4] → 7 (buy@1 sell@5 = 4, buy@3 sell@6 = 3)
#
# APPROACH: Greedy — collect every upward move.
# Profit from day i to i+1 only if price goes up (prices[i+1] > prices[i]).

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Every positive difference between consecutive days = profit we can capture
        # This is equivalent to buying at every valley and selling at every peak
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        # Time: O(n)  Space: O(1)
# @lc code=end
