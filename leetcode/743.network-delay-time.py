#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#
# PROBLEM:
# You have n nodes (1..n) and directed edges times[i]=[u,v,w] (from u to v, weight w).
# Send a signal from k. Return minimum time for all nodes to receive the signal,
# or -1 if unreachable.
# Example: times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2 → 2
#
# APPROACH: Dijkstra's algorithm from source k.
# Use a min-heap. dist[node] = shortest time to reach node.

# @lc code=start
import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {}
        heap = [(0, k)]  # (cost, node)

        while heap:
            cost, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = cost
            for weight, neighbor in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (cost + weight, neighbor))

        return max(dist.values()) if len(dist) == n else -1
        # Time: O(E log V)  Space: O(V + E)
# @lc code=end
