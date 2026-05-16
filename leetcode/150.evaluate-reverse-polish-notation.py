#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#
# PROBLEM:
# Evaluate an expression in Reverse Polish Notation (postfix).
# Valid operators: +, -, *, /  (integer division truncates toward zero)
# Example: ["2","1","+","3","*"] → 9  ((2+1)*3)
#          ["4","13","5","/","+"] → 6  (4+(13/5))
#
# APPROACH: Stack. Numbers → push. Operators → pop two, compute, push result.

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {'+', '-', '*', '/'}

        for token in tokens:
            if token in ops:
                b = stack.pop()    # second operand (right side)
                a = stack.pop()    # first operand (left side)
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    # Python // rounds toward -inf, but we need truncation toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
        # Time: O(n)  Space: O(n)
# @lc code=end
