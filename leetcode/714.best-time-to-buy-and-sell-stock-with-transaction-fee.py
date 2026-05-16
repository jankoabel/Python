#
# @lc app=leetcode id=714 lang=python
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
# PROBLEM:
# Given prices[] and a fee per transaction, find maximum profit.
# You may complete as many transactions as you want but must pay fee for each.
# You may not hold more than one share at a time.
# Example: prices=[1,3,2,8,4,9], fee=2 → 8
#
# APPROACH: DP with two states.
# hold  = max profit when currently holding a stock
# cash  = max profit when not holding a stock
# Transition:
#   hold = max(hold, cash - price)    # buy or keep holding
#   cash = max(cash, hold + price - fee)  # sell or keep cash

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        hold = float('-inf')  # haven't bought yet
        cash = 0

        for price in prices:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)

        return cash
        # Time: O(n)  Space: O(1)
# @lc code=end
