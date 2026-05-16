#
# @lc app=leetcode id=732 lang=python
#
# [732] My Calendar III (HARD)
#
# PROBLEM:
# Return the maximum k-booking (max number of overlapping events at any time).
# Implement book(start, end) which adds an event and returns max k-booking.
# Example: book(10,20)→1, book(50,60)→1, book(10,40)→2, book(5,15)→3
#
# APPROACH: Difference array / event sweep.
# At start: +1, at end: -1. Running sum gives current active events.
# Use a sorted dict for efficiency.

# @lc code=start
from sortedcontainers import SortedDict

class MyCalendarThree(object):

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start, end):
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end]   = self.diff.get(end,   0) - 1

        active = best = 0
        for delta in self.diff.values():
            active += delta
            best = max(best, active)
        return best
        # Time: O(n) per book  Space: O(n)
# @lc code=end
