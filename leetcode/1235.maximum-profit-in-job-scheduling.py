#
# @lc app=leetcode id=1235 lang=python
#
# [1235] Maximum Profit in Job Scheduling (HARD)
#
# PROBLEM:
# Given jobs with startTime, endTime, profit, find the maximum profit you can get
# without overlapping jobs.
# Example: startTime=[1,2,3,4,6], endTime=[3,5,10,6,9], profit=[20,20,100,70,60] → 150
#
# APPROACH: Sort by end time. DP with binary search.
# dp[i] = max profit considering first i jobs (sorted by end time).
# For each job i, either skip (dp[i] = dp[i-1]) or take it:
# binary search for latest job ending <= startTime[i], add its profit.

# @lc code=start
import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(endTime, startTime, profit))
        ends = [j[0] for j in jobs]
        dp = [0] * (len(jobs) + 1)  # dp[i] = max profit from first i jobs

        for i, (end, start, prof) in enumerate(jobs):
            # Binary search for latest job ending <= start
            k = bisect.bisect_right(ends, start)
            dp[i+1] = max(dp[i], dp[k] + prof)

        return dp[-1]
        # Time: O(n log n)  Space: O(n)
# @lc code=end
