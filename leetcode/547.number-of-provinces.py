#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#
# PROBLEM:
# There are n cities. isConnected[i][j]=1 means city i and j are directly connected.
# A province is a group of directly or indirectly connected cities.
# Return the total number of provinces.
# Example: isConnected=[[1,1,0],[1,1,0],[0,0,1]] → 2
#
# APPROACH: Union-Find (or DFS).
# For every pair (i,j) where isConnected[i][j]=1, union them.
# Count distinct roots at the end.

# @lc code=start
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        return sum(1 for i in range(n) if find(i) == i)
        # Time: O(n^2 * alpha(n))  Space: O(n)
# @lc code=end
