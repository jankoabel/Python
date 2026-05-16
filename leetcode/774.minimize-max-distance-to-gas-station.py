#
# @lc app=leetcode id=774 lang=python
#
# [774] Minimize Max Distance to Gas Station (HARD)
#
# PROBLEM:
# On a number line there are gas stations at positions[]. Add k new stations.
# Minimize the maximum distance between adjacent stations. Answer within 1e-6.
# Example: stations=[1,2,3,4,5,6,7,8,9,10], k=9 → 0.5
#
# APPROACH: Binary search on the answer (max distance D).
# For a given D, count how many stations we need to add to keep all gaps <= D.
# Each gap of length L needs ceil(L/D) - 1 new stations.

# @lc code=start
import math

class Solution(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        def stations_needed(D):
            return sum(math.ceil(stations[i+1] - stations[i]) // D
                       for i in range(len(stations)-1))
            # Use int division: ceil(gap/D) - 1 = int((gap-1)/D)

        def can_achieve(D):
            count = 0
            for i in range(len(stations) - 1):
                gap = stations[i+1] - stations[i]
                count += int((gap - 1e-9) / D)
            return count <= k

        lo, hi = 0, stations[-1] - stations[0]
        for _ in range(100):
            mid = (lo + hi) / 2.0
            if can_achieve(mid):
                hi = mid
            else:
                lo = mid
        return lo
        # Time: O(n log(1/eps))  Space: O(1)
# @lc code=end
