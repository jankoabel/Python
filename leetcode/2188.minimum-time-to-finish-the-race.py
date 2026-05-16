#
# @lc app=leetcode id=2188 lang=python
#
# [2188] Minimum Time to Finish the Race (HARD)
#
# PROBLEM:
# A race car needs numLaps laps. Tires[i]=[f,r]: lap j takes f*r^(j-1) time.
# Changing tires costs changeTime. Find minimum time to complete all laps.
# Example: tires=[[2,3],[3,4]], changeTime=5, numLaps=4 → 21
#
# APPROACH: DP.
# best[j] = min time to do j consecutive laps with same tire.
# dp[i] = min time to complete i laps total.
# dp[i] = min over j of (dp[i-j] + changeTime + best[j]) [j laps with new tire]

# @lc code=start
class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        INF = float('inf')
        # best[j] = min time to do j consecutive laps on any single tire
        best = [INF] * (numLaps + 1)

        for f, r in tires:
            time = f
            total = f
            for j in range(1, numLaps + 1):
                if time > changeTime + f:
                    break  # never worth staying on this tire this long
                best[j] = min(best[j], total)
                time *= r
                total += time

        dp = [INF] * (numLaps + 1)
        dp[0] = -changeTime  # offset so first tire change is free

        for i in range(1, numLaps + 1):
            for j in range(1, i + 1):
                if best[j] < INF:
                    dp[i] = min(dp[i], dp[i-j] + changeTime + best[j])

        return dp[numLaps]
        # Time: O(numLaps^2 + len(tires) * log(numLaps))  Space: O(numLaps)
# @lc code=end
