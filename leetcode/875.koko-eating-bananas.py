#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type piles: int
        :rtype: int
        """
        # Binary search on the answer (eating speed k)
        # For a given k: hours needed = sum of ceil(pile / k) for each pile
        # Find the MINIMUM k such that total hours <= h
        # Search space: [1, max(piles)]

        def can_finish(k):
            # Total hours at speed k — can we finish within h hours?
            return sum(math.ceil(p / k) for p in piles) <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid      # mid works, try smaller (minimize k)
            else:
                left = mid + 1   # mid too slow, need higher speed

        return left
        # Time: O(n log(max_pile))  Space: O(1)
# @lc code=end
