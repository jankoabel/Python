#
# @lc app=leetcode id=65 lang=python
#
# [65] Valid Number (HARD)
#
# PROBLEM:
# Given a string s, return true if it is a valid number.
# A valid number can be: integer, decimal, or those followed by 'e'/'E' and an integer.
# Example: "0" → True  ;  "e" → False  ;  ".1" → True  ;  "3e10" → True
#
# APPROACH: One-pass state tracking.
# Track: seen_digit, seen_dot, seen_e.
# Rules: e requires digit before it, dot forbidden after e,
#        digit required after e (use a separate flag).

# @lc code=start
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = seen_dot = seen_e = False
        seen_digit_after_e = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
                if seen_e:
                    seen_digit_after_e = True
            elif c in ('+', '-'):
                if i > 0 and s[i-1] not in ('e', 'E'):
                    return False
            elif c == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif c in ('e', 'E'):
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit_after_e = False
            else:
                return False

        return seen_digit and (not seen_e or seen_digit_after_e)
        # Time: O(n)  Space: O(1)
# @lc code=end
