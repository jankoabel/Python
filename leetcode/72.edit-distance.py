#
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Classic DP: dp[i][j] = min edits to convert word1[:i] to word2[:j]
        # Three operations: insert, delete, replace
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases: converting to/from empty string requires i or j deletions
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]          # characters match, no edit needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # delete from word1
                        dp[i][j-1],    # insert into word1
                        dp[i-1][j-1]   # replace
                    )

        return dp[m][n]
        # Time: O(m*n)  Space: O(m*n)
# @lc code=end
