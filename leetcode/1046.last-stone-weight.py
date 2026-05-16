#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Always smash the two heaviest stones → use a max-heap
        # Python only has min-heap → negate values to simulate max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)   # O(n) to build heap

        while len(heap) > 1:
            y = -heapq.heappop(heap)   # heaviest stone
            x = -heapq.heappop(heap)   # second heaviest

            if x != y:
                # Remainder y - x is put back (y >= x always since we popped in order)
                heapq.heappush(heap, -(y - x))
            # If x == y, both are destroyed — don't put anything back

        return -heap[0] if heap else 0
        # Time: O(n log n)  Space: O(n)
# @lc code=end
