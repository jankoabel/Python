#
# @lc app=leetcode id=1732 lang=python
#
# [1732] Find the Highest Altitude
#
# PROBLEM:
# A biker starts at altitude 0. gain[i] is the net gain between point i and i+1.
# Return the highest altitude reached.
# Example: gain=[-5,1,5,0,-7] → 1  ;  gain=[-4,-3,-2,-1,4,3,2] → 0
#
# APPROACH: Running prefix sum of gains. Track the maximum.

# @lc code=start
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        best = 0  # starts at altitude 0
        for g in gain:
            altitude += g
            best = max(best, altitude)
        return best
        # Time: O(n)  Space: O(1)
# @lc code=end
