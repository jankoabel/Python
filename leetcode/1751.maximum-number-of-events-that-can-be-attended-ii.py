#
# @lc app=leetcode id=1751 lang=python
#
# [1751] Maximum Number of Events That Can Be Attended II (HARD)
#
# PROBLEM:
# Given events[i]=[startDay, endDay, value] and k (max events to attend),
# return the max value of attending at most k non-overlapping events.
# Example: events=[[1,2,4],[3,4,3],[2,3,10]], k=2 → 10
#
# APPROACH: Sort by end time. DP with binary search.
# dp[i][j] = max value attending j events from first i events.
# For event i: either skip → dp[i-1][j], or take → dp[prev][j-1] + value[i]
# where prev = last event ending before start[i].

# @lc code=start
import bisect

class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x: x[1])
        n = len(events)
        ends = [e[1] for e in events]

        # dp[j][i] = max value attending j events from first i events
        dp = [[0] * (n + 1) for _ in range(k + 1)]

        for j in range(1, k + 1):
            for i in range(1, n + 1):
                start, end, val = events[i-1]
                # Binary search: latest event ending before start
                prev = bisect.bisect_left(ends, start)
                dp[j][i] = max(dp[j][i-1], dp[j-1][prev] + val)

        return dp[k][n]
        # Time: O(n*k*log n)  Space: O(n*k)
# @lc code=end
