#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#
# PROBLEM:
# An ugly number has only prime factors 2, 3, and 5.
# Return the nth ugly number. Sequence: 1,2,3,4,5,6,8,9,10,12,...
#
# APPROACH: DP with 3 pointers.
# Each ugly number = some previous ugly number × 2, ×3, or ×5.
# Keep 3 pointers (i2, i3, i5) — each points to the last number multiplied by that factor.
# Next ugly = min of the three candidates.

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] * n
        i2 = i3 = i5 = 0   # pointers for next multiple of 2, 3, 5

        for i in range(1, n):
            next2 = ugly[i2] * 2
            next3 = ugly[i3] * 3
            next5 = ugly[i5] * 5

            ugly[i] = min(next2, next3, next5)   # pick the smallest

            # Advance the pointer(s) that produced the minimum
            # (may advance multiple if they tie — avoids duplicates)
            if ugly[i] == next2: i2 += 1
            if ugly[i] == next3: i3 += 1
            if ugly[i] == next5: i5 += 1

        return ugly[n - 1]
        # Time: O(n)  Space: O(n)
# @lc code=end
