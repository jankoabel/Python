#
# @lc app=leetcode id=901 lang=python
#
# [901] Online Stock Span
#
# PROBLEM:
# Design a class that collects daily stock prices and returns the span of the
# current day's price (number of consecutive days before today where price <= today).
# Example: prices [100,80,60,70,60,75,85] → spans [1,1,1,2,1,4,6]
#
# APPROACH: Monotonic stack.
# Stack stores (price, span) pairs. When new price arrives, pop all entries
# with price <= new price and accumulate their spans.

# @lc code=start
class StockSpanner(object):

    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        # Absorb all previous days with price <= today
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
        # Time: O(1) amortized  Space: O(n)
# @lc code=end
