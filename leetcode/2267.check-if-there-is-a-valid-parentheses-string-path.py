#
# @lc app=leetcode id=2267 lang=python
#
# [2267] Check if There Is a Valid Parentheses String Path (HARD)
#
# PROBLEM:
# Given an m×n grid of '(' and ')', find if there's a path from top-left to
# bottom-right (only right/down moves) that forms a valid parentheses string.
# Example: grid=[["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]] → True
#
# APPROACH: DP with bitmask or set of possible open-count values.
# dp[r][c] = set of possible "open parentheses count" values when reaching (r,c).
# A count becomes valid at end if it equals 0.

# @lc code=start
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0:
            return False  # path length is always m+n-1 (must be even for valid parens)

        # dp[r][c] = set of possible open-count values
        dp = [[set() for _ in range(n)] for _ in range(m)]

        start = 1 if grid[0][0] == '(' else -1
        if start == 1:
            dp[0][0].add(1)
        # If start is ')' can't form valid (would immediately go negative)

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                delta = 1 if grid[r][c] == '(' else -1
                sources = set()
                if r > 0: sources |= dp[r-1][c]
                if c > 0: sources |= dp[r][c-1]
                for cnt in sources:
                    new_cnt = cnt + delta
                    if new_cnt >= 0:
                        dp[r][c].add(new_cnt)

        return 0 in dp[m-1][n-1]
        # Time: O(m*n*(m+n))  Space: O(m*n*(m+n))
# @lc code=end
