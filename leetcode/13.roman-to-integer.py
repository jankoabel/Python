#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#
# PROBLEM:
# Given a roman numeral string, convert it to an integer.
# Symbol values: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Subtraction rule: if a smaller value appears before a larger one, subtract it.
# e.g. IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {'I':1, 'V':5, 'X':10, 'L':50,
                  'C':100, 'D':500, 'M':1000}
        result = 0
        prev = 0

        # Walk RIGHT to LEFT — subtract if current < previous, else add
        for ch in reversed(s):
            curr = values[ch]
            if curr < prev:
                result -= curr   # subtraction rule (e.g. I before V)
            else:
                result += curr
            prev = curr

        return result
        # Time: O(n)  Space: O(1)
# @lc code=end
