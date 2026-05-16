#
# @lc app=leetcode id=1406 lang=python
#
# [1406] Stone Game III (HARD)
#
# PROBLEM:
# Alice and Bob alternate turns. Each turn the current player takes 1, 2, or 3 piles
# from the front. Return "Alice", "Bob", or "Tie" based on who has max total.
# Example: stoneValue=[1,2,3,7] → "Bob"
#
# APPROACH: DP from right to left.
# dp[i] = max score difference (current player - other) starting from index i.
# dp[i] = max over k=1,2,3 of: sum(stoneValue[i:i+k]) - dp[i+k]

# @lc code=start
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i] = best score diff from index i onward

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            total = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                total += stoneValue[i + k - 1]
                dp[i] = max(dp[i], total - dp[i + k])

        if dp[0] > 0:   return "Alice"
        if dp[0] < 0:   return "Bob"
        return "Tie"
        # Time: O(n)  Space: O(n)
# @lc code=end
