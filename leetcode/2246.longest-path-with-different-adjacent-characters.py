#
# @lc app=leetcode id=2246 lang=python
#
# [2246] Longest Path With Different Adjacent Characters
#
# PROBLEM:
# Given a tree (rooted at 0) where each node has a character,
# find the longest path where no two adjacent nodes share the same character.
# Example: parent=[-1,0,0,1,1,2], s="abacbe" → 3
#
# APPROACH: DFS — for each node, find the two longest valid chains from children.
# The path through node = top1 + top2 + 1 (if children have different char).

# @lc code=start
from collections import defaultdict

class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        children = defaultdict(list)
        for i in range(1, len(parent)):
            children[parent[i]].append(i)

        self.best = 1

        def dfs(node):
            top1 = top2 = 0
            for child in children[node]:
                length = dfs(child)
                if s[child] != s[node]:
                    if length > top1:
                        top1, top2 = length, top1
                    elif length > top2:
                        top2 = length
            self.best = max(self.best, top1 + top2 + 1)
            return top1 + 1

        dfs(0)
        return self.best
        # Time: O(n)  Space: O(n)
# @lc code=end
