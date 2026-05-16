#
# @lc app=leetcode id=403 lang=python
#
# [403] Frog Jump (HARD)
#
# PROBLEM:
# A frog starts at stone 0. From stone at position p with last jump k,
# the frog can jump to p+k-1, p+k, or p+k+1.
# Return true if the frog can reach the last stone.
# Example: stones=[0,1,3,5,6,8,12,17] → True
#
# APPROACH: DP with hash map.
# dp[pos] = set of jump sizes that can reach pos.
# For each stone and each possible jump size, try ±1 next jumps.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        stone_set = set(stones)
        dp = defaultdict(set)
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                for nxt_jump in (k-1, k, k+1):
                    if nxt_jump > 0 and stone + nxt_jump in stone_set:
                        dp[stone + nxt_jump].add(nxt_jump)

        return bool(dp[stones[-1]])
        # Time: O(n^2)  Space: O(n^2)
# @lc code=end
