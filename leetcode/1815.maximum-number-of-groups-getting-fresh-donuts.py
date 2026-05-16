#
# @lc app=leetcode id=1815 lang=python
#
# [1815] Maximum Number of Groups Getting Fresh Donuts (HARD)
#
# PROBLEM:
# Batchsize donuts are made per batch. Groups arrive and wait or get fresh donuts.
# A group is "happy" if they arrive at start of a batch.
# Maximize number of happy groups.
# Example: batchSize=3, groups=[1,2,3,4,5,6] → 4
#
# APPROACH: Bitmask DP (or greedy).
# Groups mod batchSize. Pair complements (0 with 0, remainder r with batchSize-r).
# Pairs both get fresh. Remaining: DP with current remainder as state.

# @lc code=start
from collections import Counter
from functools import lru_cache

class Solution(object):
    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        # Count groups by their size mod batchSize
        remainders = Counter(g % batchSize for g in groups)

        result = remainders[0]  # Groups with no remainder always happy (start fresh)

        # Pair complements: r and (batchSize - r)
        pairs = []
        for r in range(1, (batchSize // 2) + 1):
            opp = batchSize - r
            if r == opp:  # batchSize even, middle remainder
                result += remainders[r] // 2
                remainders[r] %= 2
            else:
                pair_count = min(remainders[r], remainders[opp])
                result += pair_count
                remainders[r] -= pair_count
                remainders[opp] -= pair_count
            pairs.append(remainders[r] if r <= batchSize // 2 else 0)

        # Remaining: bitmask DP on remainders
        rem_list = []
        for r in range(1, batchSize):
            rem_list.extend([r] * remainders[r])

        @lru_cache(maxsize=None)
        def dp(cur_rem, idx):
            if idx == len(rem_list):
                return 0
            r = rem_list[idx]
            happy = 1 if cur_rem == 0 else 0
            return happy + dp((cur_rem + r) % batchSize, idx + 1)

        result += dp(0, 0)
        return result
        # Time: O(batchSize * 2^n)  Space: O(batchSize * n)
# @lc code=end
