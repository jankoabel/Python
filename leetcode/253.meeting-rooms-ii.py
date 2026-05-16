#
# @lc app=leetcode id=253 lang=python
#
# [253] Meeting Rooms II
#

# @lc code=start
import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Greedy with a min-heap of end times
        # Sort by start time. For each meeting, check if earliest-ending room is free.
        # If yes → reuse that room (update its end time)
        # If no  → open a new room
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])   # sort by start time
        heap = []   # min-heap of end times of currently occupied rooms

        for start, end in intervals:
            if heap and heap[0] <= start:
                # Earliest-finishing room is free before this meeting starts
                heapq.heapreplace(heap, end)   # reuse the room, update end time
            else:
                heapq.heappush(heap, end)      # need a new room

        return len(heap)   # number of rooms in use = max overlap
        # Time: O(n log n)  Space: O(n)
# @lc code=end
