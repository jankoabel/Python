#
# @lc app=leetcode id=1192 lang=python
#
# [1192] Critical Connections in a Network (HARD)
#
# PROBLEM:
# Given a connected network of n servers and connections, find all critical
# connections (bridges) — removing any one disconnects the network.
# Example: n=4, connections=[[0,1],[1,2],[2,0],[1,3]] → [[1,3]]
#
# APPROACH: Tarjan's bridge-finding algorithm.
# DFS with discovery times and low values.
# Edge (u,v) is a bridge if low[v] > disc[u] (v can't reach u's subtree without u→v).

# @lc code=start
from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        disc = [-1] * n
        low  = [-1] * n
        bridges = []
        self.timer = 0

        def dfs(node, parent):
            disc[node] = low[node] = self.timer
            self.timer += 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if disc[neighbor] == -1:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        bridges.append([node, neighbor])
                else:
                    low[node] = min(low[node], disc[neighbor])

        dfs(0, -1)
        return bridges
        # Time: O(V + E)  Space: O(V + E)
# @lc code=end
