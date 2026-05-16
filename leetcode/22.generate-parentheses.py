#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
# PROBLEM:
# Given n pairs of parentheses, generate all combinations of well-formed parentheses.
# Example: n=3 → ["((()))","(()())","(())()","()(())","()()()"]
#
# APPROACH: Backtracking with validity constraints.
# At each step: add '(' if open_count < n
#               add ')' if close_count < open_count

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:    # used all n pairs
                result.append(''.join(current))
                return

            if open_count < n:           # can still open a bracket
                current.append('(')
                backtrack(current, open_count + 1, close_count)
                current.pop()

            if close_count < open_count: # can close only if more opens exist
                current.append(')')
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result
        # Time: O(4^n / sqrt(n)) — Catalan number  Space: O(n)
# @lc code=end
