#
# @lc app=leetcode id=224 lang=python
#
# [224] Basic Calculator (HARD)
#
# PROBLEM:
# Given a string expression with +, -, (, ), spaces. Evaluate and return the result.
# Example: s="1 + 1" → 2  ;  s="(1+(4+5+2)-3)+(6+8)" → 23
#
# APPROACH: Stack-based.
# Track current number, current sign (+1 or -1), and result.
# On '(': push (result, sign) and reset; on ')': pop and combine.

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        num = 0
        sign = 1  # +1 or -1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                result += sign * num
                num = 0
                sign = 1
            elif c == '-':
                result += sign * num
                num = 0
                sign = -1
            elif c == '(':
                # Save current state and start fresh
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += sign * num
                num = 0
                result *= stack.pop()   # sign before '('
                result += stack.pop()   # result before '('

        return result + sign * num
        # Time: O(n)  Space: O(n)
# @lc code=end
