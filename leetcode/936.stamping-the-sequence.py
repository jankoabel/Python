#
# @lc app=leetcode id=936 lang=python
#
# [936] Stamping The Sequence (HARD)
#
# PROBLEM:
# You have a stamp and a target string. In each move, place stamp at some position
# to overwrite that substring. Return a sequence of positions to stamp that
# produces target. Use at most 10 * target.length moves.
# Example: stamp="abc", target="ababc" → [0,2] or [2,0,2]
#
# APPROACH: Work backwards — un-stamp target.
# Find a window that matches stamp (possibly partially, with wildcards '*').
# Replace it with '*'s. Repeat until all '*'. Reverse the order.

# @lc code=start
class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        S, T = len(stamp), len(target)
        target = list(target)
        result = []
        total_stamped = 0
        stamped = True

        while stamped:
            stamped = False
            for i in range(T - S + 1):
                # Count stars already in window and check remaining chars match stamp
                stars = 0
                match = True
                for j in range(S):
                    if target[i+j] == '*':
                        stars += 1
                    elif target[i+j] != stamp[j]:
                        match = False
                        break

                if match and stars < S:  # at least 1 new char stamped
                    for j in range(S):
                        target[i+j] = '*'
                    total_stamped += S - stars
                    result.append(i)
                    stamped = True

        if total_stamped == T:
            return result[::-1]
        return []
        # Time: O((T-S) * S * T)  Space: O(T)
# @lc code=end
