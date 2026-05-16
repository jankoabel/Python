#
# @lc app=leetcode id=301 lang=python
#
# [301] Remove Invalid Parentheses (HARD)
#
# PROBLEM:
# Remove the minimum number of invalid parentheses from string s and return
# all valid results.
# Example: s="()())()" → ["(())()","()()()"]
#
# APPROACH: BFS from original string. Level by level (each level removes one char).
# First level with a valid string: collect all valid ones and stop.

# @lc code=start
from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(t):
            count = 0
            for c in t:
                if c == '(':   count += 1
                elif c == ')':
                    count -= 1
                    if count < 0: return False
            return count == 0

        visited = {s}
        queue = deque([s])
        result = []
        found = False

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()
                if is_valid(curr):
                    result.append(curr)
                    found = True
                if found:
                    continue
                for i, c in enumerate(curr):
                    if c not in '()':
                        continue
                    nxt = curr[:i] + curr[i+1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            if found:
                break

        return result
        # Time: O(2^n * n)  Space: O(2^n)
# @lc code=end
