#
# @lc app=leetcode id=1466 lang=python
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#
# PROBLEM:
# There are n cities and n-1 directed edges. Reorder minimum edges so all cities
# can reach city 0.
# Example: n=6, connections=[[0,1],[1,3],[2,3],[4,0],[4,5]] → 3
#
# APPROACH: BFS from city 0 on the undirected graph.
# Count original edges that go "away" from 0 (need to be reversed).
# Build adjacency list with weights: 1 = original direction, 0 = reverse.

# @lc code=start
from collections import deque, defaultdict

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # original direction costs 1 reversal
            graph[b].append((a, 0))  # reverse direction costs 0

        visited = set([0])
        queue = deque([0])
        changes = 0

        while queue:
            node = queue.popleft()
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    changes += cost
                    queue.append(neighbor)

        return changes
        # Time: O(n)  Space: O(n)
# @lc code=end
