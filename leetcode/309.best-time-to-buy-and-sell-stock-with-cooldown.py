#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # State machine DP with 3 states:
        #   held    = max profit when currently holding a stock
        #   sold    = max profit on day we just sold (enters cooldown next day)
        #   rest    = max profit when in cooldown or idle (can buy next day)
        #
        # Transitions:
        #   held = max(held, rest - price)   buy today or keep holding
        #   sold = held + price               sell today
        #   rest = max(rest, sold)            cooldown passes or stay idle
        held = float('-inf')
        sold = 0
        rest = 0

        for price in prices:
            prev_held = held
            held = max(held, rest - price)   # keep holding OR buy (can only buy from rest state)
            rest = max(rest, sold)            # stay idle OR come off cooldown
            sold = prev_held + price          # sell what we were holding

        return max(sold, rest)   # don't want to end holding stock
        # Time: O(n)  Space: O(1)
# @lc code=end
