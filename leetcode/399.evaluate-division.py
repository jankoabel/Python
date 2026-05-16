#
# @lc app=leetcode id=399 lang=python
#
# [399] Evaluate Division
#
# PROBLEM:
# You are given equations like A/B = k. Given queries A/B, return the answers.
# If answer doesn't exist, return -1.
# Example: equations=[["a","b"],["b","c"]], values=[2.0,3.0]
#          queries=[["a","c"],["b","a"]] → [6.0, 0.5]
#
# APPROACH: Build a weighted directed graph. A→B has weight k, B→A has weight 1/k.
# For each query, DFS/BFS from source to destination, multiplying edge weights.

# @lc code=start
from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited = set()
            queue = deque([(src, 1.0)])
            while queue:
                node, product = queue.popleft()
                if node == dst:
                    return product
                visited.add(node)
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * weight))
            return -1.0

        return [bfs(a, b) for a, b in queries]
        # Time: O(Q * (V + E))  Space: O(V + E)
# @lc code=end
