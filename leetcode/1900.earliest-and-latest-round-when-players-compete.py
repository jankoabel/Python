#
# @lc app=leetcode id=1900 lang=python
#
# [1900] The Earliest and Latest Round When Players Compete (HARD)
#
# PROBLEM:
# n players compete. In each round, player 1 vs player n, 2 vs n-1, etc.
# Winners advance. Player firstPlayer and secondPlayer always win (unless they
# face each other). Return [earliest, latest] round when they compete.
#
# APPROACH: Memoized DFS on state (left, right, n) where left/right are positions
# of the two special players from each end. Simulate all possible outcomes.

# @lc code=start
from functools import lru_cache

class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        @lru_cache(maxsize=None)
        def dp(left, right, total):
            # left, right = positions from left/right end (1-indexed)
            # total = current number of players
            if left + right == total + 1:
                return (1, 1)  # they meet this round
            # Ensure left < right from same direction
            if left > total + 1 - right:
                left, right = total + 1 - right, total + 1 - left

            half = total // 2
            earliest, latest = float('inf'), float('-inf')

            # Enumerate: how many players before left win, how many between win
            for wins_before in range(left):  # 0..left-1 players before left win
                for wins_between in range(right - left - 1 + 1):  # players between
                    # New positions after this round
                    new_left  = wins_before + 1
                    new_right = wins_before + wins_between + 2
                    new_total = (total + 1) // 2
                    if new_left < 1 or new_right > new_total:
                        continue
                    a, b = dp(new_left, new_right, new_total)
                    earliest = min(earliest, a + 1)
                    latest   = max(latest,   b + 1)

            return (earliest, latest)

        fp = min(firstPlayer, secondPlayer)
        sp = max(firstPlayer, secondPlayer)
        return list(dp(fp, n + 1 - sp, n))
        # Time: O(n^3) states  Space: O(n^2)
# @lc code=end
