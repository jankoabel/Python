#
# @lc app=leetcode id=785 lang=python
#
# [785] Is Graph Bipartite?
#
# PROBLEM:
# There is an undirected graph with n nodes. Given its adjacency list,
# return true if the graph is bipartite (can be 2-colored with no same-color edges).
# Example: graph=[[1,2,3],[0,2],[0,1,3],[0,2]] → False
#
# APPROACH: BFS/DFS coloring.
# Try to 2-color the graph: assign color 0 or 1 alternately.
# If we ever find a neighbor with the same color → not bipartite.

# @lc code=start
from collections import deque

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [-1] * n  # -1 = unvisited

        for start in range(n):
            if color[start] != -1:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]  # opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False  # same color on both ends of an edge

        return True
        # Time: O(V + E)  Space: O(V)
# @lc code=end
