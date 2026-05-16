#
# @lc app=leetcode id=352 lang=python
#
# [352] Data Stream as Disjoint Intervals (HARD)
#
# PROBLEM:
# Design a SummaryRanges class that:
# - addNum(val): adds an integer from the data stream
# - getIntervals(): returns a summary of numbers as disjoint intervals
# Example: addNum 1,3,7,2,6 → getIntervals → [[1,3],[6,7]]
#
# APPROACH: Use a sorted list of intervals. On addNum, find where val fits
# and merge with adjacent intervals if needed.

# @lc code=start
import bisect

class SummaryRanges(object):

    def __init__(self):
        self.intervals = []  # sorted list of [start, end]

    def addNum(self, val):
        new = [val, val]
        intervals = self.intervals
        # Find insertion position
        lo = bisect.bisect_left(intervals, [val])
        # Check if merges with previous interval
        if lo > 0 and intervals[lo-1][1] >= val - 1:
            lo -= 1
            new[0] = min(new[0], intervals[lo][0])
        hi = lo
        # Check if merges with subsequent intervals
        while hi < len(intervals) and intervals[hi][0] <= val + 1:
            new[1] = max(new[1], intervals[hi][1])
            hi += 1
        self.intervals[lo:hi] = [new]

    def getIntervals(self):
        return self.intervals
        # Time: addNum O(n), getIntervals O(1)  Space: O(n)
# @lc code=end
