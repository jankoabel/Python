#
# @lc app=leetcode id=834 lang=python
#
# [834] Sum of Distances in Tree (HARD)
#
# PROBLEM:
# Given an undirected tree with n nodes, return an array where answer[i] is
# the sum of distances from node i to all other nodes.
# Example: n=6, edges=[[0,1],[0,2],[2,3],[2,4],[2,5]] → [8,12,6,10,10,10]
#
# APPROACH: Two DFS passes.
# Pass 1: Root at 0. Compute subtree size and answer[0] (total distance from root).
# Pass 2: Re-root — when moving to child c: answer[c] = answer[root] - size[c] + (n - size[c])

# @lc code=start
from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = [1] * n   # subtree sizes
        answer = [0] * n

        # DFS 1: count subtree sizes and answer[0]
        def dfs1(node, parent, depth):
            answer[0] += depth
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node, depth + 1)
                    count[node] += count[child]

        # DFS 2: re-root
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs1(0, -1, 0)
        dfs2(0, -1)
        return answer
        # Time: O(n)  Space: O(n)
# @lc code=end
