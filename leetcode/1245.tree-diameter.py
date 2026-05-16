#
# @lc app=leetcode id=1245 lang=python
#
# [1245] Tree Diameter (HARD)
#
# PROBLEM:
# Given an undirected tree, return the length of the longest path (diameter).
# Example: edges=[[0,1],[0,2]] → 2  ;  edges=[[0,1],[1,2],[2,3],[1,4],[4,5]] → 4
#
# APPROACH: DFS — for each node, compute the longest paths through its two children.
# The diameter through node = top1_depth + top2_depth.
# Return the max depth to parent.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return 0
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.diameter = 0

        def dfs(node, parent):
            top1 = top2 = 0  # two longest paths from this node
            for child in graph[node]:
                if child == parent:
                    continue
                depth = dfs(child, node) + 1
                if depth > top1:
                    top1, top2 = depth, top1
                elif depth > top2:
                    top2 = depth
            self.diameter = max(self.diameter, top1 + top2)
            return top1

        dfs(0, -1)
        return self.diameter
        # Time: O(n)  Space: O(n)
# @lc code=end
