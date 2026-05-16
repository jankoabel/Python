#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III (HARD)
#
# PROBLEM:
# You may complete at most 2 transactions.
# Find the maximum profit.
# Example: [3,3,5,0,0,3,1,4] → 6 (buy@0 sell@3 = 3, buy@1 sell@4 = 3)
#
# APPROACH: Track 4 states:
# buy1:  max profit after 1st buy   (negative because spent money)
# sell1: max profit after 1st sell
# buy2:  max profit after 2nd buy
# sell2: max profit after 2nd sell

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        for price in prices:
            buy1  = max(buy1,  -price)          # best profit buying today (first purchase)
            sell1 = max(sell1, buy1 + price)    # best profit selling today (first sale)
            buy2  = max(buy2,  sell1 - price)   # best profit buying today (second purchase)
            sell2 = max(sell2, buy2 + price)    # best profit selling today (second sale)

        return sell2
        # Time: O(n)  Space: O(1)
# @lc code=end
