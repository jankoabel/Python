#
# @lc app=leetcode id=323 lang=python
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Union-Find (Disjoint Set Union): merge nodes that share an edge
        # Count remaining distinct roots = number of components
        parent = list(range(n))   # each node starts as its own parent
        rank = [1] * n

        def find(x):
            # Path compression: point all nodes directly to root
            while parent[x] != x:
                parent[x] = parent[parent[x]]   # two-step path halving
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return 0   # already in same component
            # Union by rank: attach smaller tree under larger
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return 1   # merged two components

        components = n
        for u, v in edges:
            components -= union(u, v)   # each successful merge reduces count by 1

        return components
        # Time: O(n + e * α(n)) ≈ O(n + e)  Space: O(n)
# @lc code=end
