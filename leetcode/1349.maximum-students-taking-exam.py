#
# @lc app=leetcode id=1349 lang=python
#
# [1349] Maximum Students Taking Exam (HARD)
#
# PROBLEM:
# In a seat grid ('.' = good seat, '#' = broken), students cannot sit adjacent
# (L/R) or diagonally adjacent upper-row. Maximize students seated.
# Example: seats=[[".","#"],["#","."],[".","."]] → 4
#
# APPROACH: Bitmask DP row by row.
# dp[row][mask] = max students when row's students sit in positions given by mask.
# Constraints: no two set bits adjacent, no bit conflicts with '#', no diagonal attack.

# @lc code=start
class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        m, n = len(seats), len(seats[0])

        # Convert each row to bitmask of valid seats
        valid = []
        for row in seats:
            mask = 0
            for c, s in enumerate(row):
                if s == '.':
                    mask |= (1 << c)
            valid.append(mask)

        dp = {0: 0}  # prev_mask → max students

        for r in range(m):
            new_dp = {}
            # Enumerate valid masks for this row
            for mask in range(1 << n):
                if mask & valid[r] != mask: continue      # must sit in valid seats
                if mask & (mask >> 1): continue           # no two adjacent in same row

                for prev_mask, prev_count in dp.items():
                    # No diagonal attacks from previous row
                    if mask & (prev_mask << 1): continue  # upper-left attack
                    if mask & (prev_mask >> 1): continue  # upper-right attack

                    count = prev_count + bin(mask).count('1')
                    if mask not in new_dp or new_dp[mask] < count:
                        new_dp[mask] = count

            dp = new_dp

        return max(dp.values()) if dp else 0
        # Time: O(m * 4^n)  Space: O(2^n)
# @lc code=end
