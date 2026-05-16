#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Use a MAX-heap of size k (negate distances to simulate max-heap with Python's min-heap)
        # If heap has k elements and new point is closer than the farthest → swap it in
        # This keeps only the k closest points at all times
        heap = []   # stores (-distance_squared, x, y)

        for x, y in points:
            dist = -(x*x + y*y)   # negate because Python heap is min-heap
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:   # closer than the current farthest in heap
                heapq.heapreplace(heap, (dist, x, y))

        return [[x, y] for _, x, y in heap]
        # Time: O(n log k)  Space: O(k)
# @lc code=end
