#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#
# PROBLEM:
# Implement atoi which converts a string to an integer.
# Rules: skip leading whitespace, read optional sign (+/-),
# read digits until non-digit or end. Clamp to 32-bit signed int range.

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()          # step 1: skip leading whitespace
        if not s:
            return 0

        sign = 1
        i = 0

        # step 2: read optional sign
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            i = 1

        # step 3: read digits
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # step 4: clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, result))
        # Time: O(n)  Space: O(1)
# @lc code=end
