#
# @lc app=leetcode id=1857 lang=python
#
# [1857] Largest Color Value in a Directed Graph (HARD)
#
# PROBLEM:
# Given a directed graph where each node has a color (char), find the largest
# number of nodes with the same color on any valid path. Return -1 if cycle.
# Example: colors="abaca", edges=[[0,1],[0,2],[2,3],[3,4]] → 3 ("a" appears 3 times on path 0→2→3→4)
#
# APPROACH: Topological sort (Kahn's BFS).
# dp[node][c] = max count of color c on any path ending at node.
# If not all nodes processed → cycle → return -1.

# @lc code=start
from collections import defaultdict, deque

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        graph = defaultdict(list)
        indeg = [0] * n

        for a, b in edges:
            graph[a].append(b)
            indeg[b] += 1

        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1

        queue = deque([i for i in range(n) if indeg[i] == 0])
        processed = 0
        result = 0

        while queue:
            node = queue.popleft()
            processed += 1
            result = max(result, max(dp[node]))
            for nb in graph[node]:
                for c in range(26):
                    dp[nb][c] = max(dp[nb][c], dp[node][c] + (1 if ord(colors[nb]) - ord('a') == c else 0))
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    queue.append(nb)

        return result if processed == n else -1
        # Time: O(V*26 + E)  Space: O(V*26)
# @lc code=end
