#
# @lc app=leetcode id=2421 lang=python
#
# [2421] Number of Good Paths (HARD)
#
# PROBLEM:
# A good path starts and ends at nodes with the same value and all intermediate
# nodes have values <= that value.
# Count the total number of good paths (including trivial single-node paths).
# Example: vals=[1,3,2,1,3], edges=[[0,1],[0,2],[2,3],[2,4]] → 6
#
# APPROACH: Sort edges by max(vals[u], vals[v]). Process in increasing order.
# Union-Find: when we add an edge, check if both endpoints can form good paths.
# For each node with same val in same component: add paths between them.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(vals)
        parent = list(range(n))
        count = [1] * n  # count of max-value nodes in each component

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return 0
            # Merge by value (not rank): the higher value component dominates
            if vals[rx] < vals[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            good = 0
            if vals[rx] == vals[ry]:
                good = count[rx] * count[ry]
                count[rx] += count[ry]
            return good

        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))
        result = n  # each single node is a trivial good path

        for u, v in edges:
            result += union(u, v)

        return result
        # Time: O(n log n)  Space: O(n)
# @lc code=end
