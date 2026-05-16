#
# @lc app=leetcode id=1499 lang=python
#
# [1499] Max Value of Equation (HARD)
#
# PROBLEM:
# Given sorted points[[xi,yi]] and k, find max (yi + yj + |xi - xj|)
# where |xi - xj| <= k and i < j. Simplifies to max (yj + xj) + (yi - xi) where xj-xi<=k.
# Example: points=[[1,3],[2,0],[5,10],[6,-10]], k=1 → 4
#
# APPROACH: Monotonic deque.
# For each j, we want max(yi - xi) for all i < j with xj - xi <= k.
# Maintain a deque of (yi-xi, xi) in decreasing order of (yi-xi).
# Pop from front if too far (xi < xj - k).

# @lc code=start
from collections import deque

class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        dq = deque()  # (yi - xi, xi) in decreasing order
        result = float('-inf')

        for xj, yj in points:
            # Remove points too far to the left
            while dq and xj - dq[0][1] > k:
                dq.popleft()
            # Best candidate gives maximum value
            if dq:
                result = max(result, yj + xj + dq[0][0])
            # Maintain decreasing deque
            while dq and dq[-1][0] <= yj - xj:
                dq.pop()
            dq.append((yj - xj, xj))

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
