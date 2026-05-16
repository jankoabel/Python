#
# @lc app=leetcode id=2141 lang=python
#
# [2141] Maximum Running Time of N Computers (HARD)
#
# PROBLEM:
# n computers powered by batteries. Batteries can be swapped but one computer
# needs one battery at a time. Maximize minutes all n computers run simultaneously.
# Example: n=2, batteries=[3,3,3] → 4
#
# APPROACH: Binary search on answer T (total minutes all n run).
# For given T, each battery contributes min(battery, T) minutes.
# Total contribution >= n*T means T is achievable.

# @lc code=start
class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        total = sum(batteries)
        lo, hi = 1, total // n

        while lo < hi:
            mid = (lo + hi + 1) // 2
            # Each battery contributes min(battery, mid) to total capacity
            if sum(min(b, mid) for b in batteries) >= n * mid:
                lo = mid
            else:
                hi = mid - 1

        return lo
        # Time: O(m log(sum/n))  Space: O(1)
# @lc code=end
