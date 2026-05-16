#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#
# PROBLEM:
# Given an integer n, return the minimum number of perfect square numbers
# that sum to n. (Perfect squares: 1,4,9,16,...)
# Example: n=12 → 3 (4+4+4)  ;  n=13 → 2 (4+9)
#
# APPROACH: DP — similar to Coin Change but coins are perfect squares.
# dp[i] = minimum number of squares summing to i.

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0   # 0 squares needed to make 0

        # Precompute perfect squares up to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        for amount in range(1, n + 1):
            for sq in squares:
                if sq > amount:
                    break
                # Use square sq: one square + however many needed for (amount - sq)
                dp[amount] = min(dp[amount], dp[amount - sq] + 1)

        return dp[n]
        # Time: O(n * sqrt(n))  Space: O(n)
# @lc code=end
