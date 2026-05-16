#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses (HARD)
#
# PROBLEM:
# Given a string of '(' and ')', return the length of the longest valid
# (well-formed) parentheses substring.
# Example: s="(()" → 2  ;  s=")()())" → 4  ;  s="" → 0
#
# APPROACH: Stack — push index of '(' or reset on unmatched ')'.
# Initialize stack with [-1] as a base index.
# - '(': push index
# - ')': pop; if stack empty push current index (new base); else update max = i - stack[-1]

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # base index for calculating lengths
        best = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # unmatched ')' becomes new base
                else:
                    best = max(best, i - stack[-1])

        return best
        # Time: O(n)  Space: O(n)
# @lc code=end
