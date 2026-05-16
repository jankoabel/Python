#
# @lc app=leetcode id=787 lang=python
#
# [787] Cheapest Flights Within K Stops
#
# PROBLEM:
# There are n cities and m flights. Each flight is (from, to, price).
# Find the cheapest price from src to dst with at most k stops.
# Return -1 if no such route exists.
# Example: n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1 → 200
#
# APPROACH: Bellman-Ford with k+1 rounds.
# prices[v] = min cost to reach v in at most i edges after i rounds.
# Important: use a copy of prices at start of each round to avoid using new edges twice.

# @lc code=start
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float('inf')
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):  # at most k+1 edges = k stops
            temp = prices[:]    # snapshot — prevents using this round's updates
            for u, v, w in flights:
                if prices[u] < INF:
                    temp[v] = min(temp[v], prices[u] + w)
            prices = temp

        return prices[dst] if prices[dst] < INF else -1
        # Time: O(k * E)  Space: O(n)
# @lc code=end
