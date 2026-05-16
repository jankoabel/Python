#
# @lc app=leetcode id=261 lang=python
#
# [261] Graph Valid Tree
#

# @lc code=start
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # A valid tree has exactly two properties:
        # 1. n-1 edges (fewer = disconnected, more = cycle)
        # 2. All nodes are connected (one component)
        if len(edges) != n - 1:
            return False   # quick check: tree must have exactly n-1 edges

        # DFS to verify all nodes are reachable from node 0
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        return len(visited) == n   # all nodes must be reachable
        # Time: O(n + e)  Space: O(n)
# @lc code=end
