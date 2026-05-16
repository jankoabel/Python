#
# @lc app=leetcode id=252 lang=python
#
# [252] Meeting Rooms
#

# @lc code=start
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # Sort by start time. If any meeting starts before the previous one ends → conflict.
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            # Previous meeting ends AFTER current one starts → overlap
            if intervals[i-1][1] > intervals[i][0]:
                return False

        return True
        # Time: O(n log n)  Space: O(1)
# @lc code=end
