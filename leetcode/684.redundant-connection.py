#
# @lc app=leetcode id=684 lang=python
#
# [684] Redundant Connection
#

# @lc code=start
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Union-Find: add edges one by one
        # The first edge that connects two already-connected nodes creates a cycle
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]   # path compression
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False   # already connected → this edge is redundant
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]   # this edge caused a cycle
        # Time: O(n * α(n)) ≈ O(n)  Space: O(n)
# @lc code=end
