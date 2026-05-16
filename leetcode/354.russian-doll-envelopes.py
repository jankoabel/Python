#
# @lc app=leetcode id=354 lang=python
#
# [354] Russian Doll Envelopes (HARD)
#
# PROBLEM:
# You have envelopes with (width, height). One envelope can fit inside another
# only if BOTH width AND height are strictly larger.
# Return the maximum number of envelopes you can nest.
# Example: [[5,4],[6,4],[6,7],[2,3]] → 3 (envelope [2,3] → [5,4] → [6,7])
#
# APPROACH: Sort by width ascending. For same width, sort height DESCENDING.
# Then find LIS on heights only.
# Why descending for same width? Prevents using two same-width envelopes
# (same width can't strictly fit — descending heights means LIS picks at most one).

# @lc code=start
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Sort: width ascending, height DESCENDING for same width
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # LIS on heights using binary search (patience sorting) — O(n log n)
        tails = []
        for _, h in envelopes:
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < h:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(tails):
                tails.append(h)
            else:
                tails[lo] = h

        return len(tails)
        # Time: O(n log n)  Space: O(n)
# @lc code=end
