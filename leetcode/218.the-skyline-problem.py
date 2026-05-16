#
# @lc app=leetcode id=218 lang=python
#
# [218] The Skyline Problem (HARD)
#
# PROBLEM:
# Given buildings as [left, right, height], compute the skyline (list of key points).
# A key point is [x, y] where the max height changes.
# Example: buildings=[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#          → [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
#
# APPROACH: Event-based sweep line with a max-heap.
# Events: building start (negative height = add), building end (remove).
# At each x-coordinate, track the current max height. When it changes, record it.

# @lc code=start
import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))  # start: negative height
            events.append((r,  0, 0))  # end event
        events.sort()

        result = [[0, 0]]  # sentinel
        heap = [(0, float('inf'))]  # (neg_height, end_x)

        for x, neg_h, end in events:
            # Add new building
            if neg_h != 0:
                heapq.heappush(heap, (neg_h, end))
            # Remove expired buildings
            while heap[0][1] <= x:
                heapq.heappop(heap)
            # Check if max height changed
            cur_max = -heap[0][0]
            if cur_max != result[-1][1]:
                result.append([x, cur_max])

        return result[1:]
        # Time: O(n log n)  Space: O(n)
# @lc code=end
