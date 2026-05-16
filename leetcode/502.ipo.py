#
# @lc app=leetcode id=502 lang=python
#
# [502] IPO (HARD)
#
# PROBLEM:
# Given k projects to pick, starting capital w, profits[] and capital[] per project,
# maximize final capital. You can do at most k projects.
# Example: k=2, w=0, profits=[1,2,3], capital=[0,1,1] → 4
#
# APPROACH: Greedy + two heaps.
# Sort projects by capital. Use a min-heap to track available projects.
# At each step: move all affordable projects to a max-heap, pick the best profit.

# @lc code=start
import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = sorted(zip(capital, profits))
        max_heap = []  # negate profits for max-heap
        i = 0

        for _ in range(k):
            # Add all newly affordable projects
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            w += -heapq.heappop(max_heap)

        return w
        # Time: O((n+k) log n)  Space: O(n)
# @lc code=end
