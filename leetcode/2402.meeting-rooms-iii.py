#
# @lc app=leetcode id=2402 lang=python
#
# [2402] Meeting Rooms III (HARD)
#
# PROBLEM:
# n meeting rooms (0..n-1). Meetings[i]=[start,end]. Each meeting uses the lowest-
# numbered available room. If no room is free, delay until one frees.
# Return the room used most. Ties: smallest index.
# Example: n=2, meetings=[[0,10],[1,5],[2,7],[3,4]] → 0
#
# APPROACH: Two heaps.
# available: min-heap of free room indices.
# busy: min-heap of (end_time, room_index) for occupied rooms.

# @lc code=start
import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        count = [0] * n
        available = list(range(n))  # min-heap of free rooms
        heapq.heapify(available)
        busy = []  # (end_time, room_idx)

        for start, end in meetings:
            # Free up rooms that have finished
            while busy and busy[0][0] <= start:
                end_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Use earliest-ending room
                earliest_end, room = heapq.heappop(busy)
                heapq.heappush(busy, (earliest_end + (end - start), room))

            count[room] += 1

        return count.index(max(count))
        # Time: O(m log m + m log n)  Space: O(n)
# @lc code=end
