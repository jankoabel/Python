#
# @lc app=leetcode id=920 lang=python
#
# [920] Number of Music Playlists (HARD)
#
# PROBLEM:
# You want a playlist of length goal with n unique songs. Rules:
# - Every song must be played at least once
# - A song can only be replayed if k other songs have been played since last play
# Return number of possible playlists (mod 10^9+7).
# Example: goal=3, n=3, k=1 → 6
#
# APPROACH: DP. dp[i][j] = playlists of length i using exactly j unique songs.
# dp[i][j] = dp[i-1][j-1] * (n - (j-1))  # add a new song
#           + dp[i-1][j]   * max(j-k, 0)  # replay an old song (must have j-k choices)

# @lc code=start
class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Add a new unique song
                dp[i][j] += dp[i-1][j-1] * (n - (j-1))
                # Replay an old song (must have j-k options available)
                dp[i][j] += dp[i-1][j] * max(j - k, 0)
                dp[i][j] %= MOD

        return dp[goal][n]
        # Time: O(goal * n)  Space: O(goal * n)
# @lc code=end
