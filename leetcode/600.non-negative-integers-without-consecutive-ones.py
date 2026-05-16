#
# @lc app=leetcode id=600 lang=python
#
# [600] Non-negative Integers without Consecutive Ones (HARD)
#
# PROBLEM:
# Given n, find how many integers in [0, n] have no consecutive 1s in binary.
# Example: n=5 → 5 (0,1,2,4,5 have no consecutive ones; 3=11 does)
#
# APPROACH: Digit DP on binary representation.
# dp[i][j] = count of valid i-bit numbers ending in bit j (0 or 1).
# Base: dp[1][0]=1 (just "0"), dp[1][1]=1 (just "1").
# Transition: dp[i][0] = dp[i-1][0] + dp[i-1][1]  (can follow either 0 or 1)
#             dp[i][1] = dp[i-1][0]                  (can only follow 0)
# Then walk n's bits and count valid numbers below n.

# @lc code=start
class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = bin(n)[2:]
        m = len(bits)

        # dp[i][j] = count of valid numbers with i bits ending in j
        dp = [[0, 0] for _ in range(m + 1)]
        dp[1][0] = dp[1][1] = 1

        for i in range(2, m + 1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]

        result = 0
        prev_bit = 0
        for i, bit in enumerate(bits):
            bit = int(bit)
            if bit == 1:
                # Count numbers with 0 at this position (then any valid suffix)
                result += dp[m - i][0]
                if prev_bit == 1:
                    # Consecutive ones found in n — stop
                    break
            prev_bit = bit
            if i == m - 1:
                result += 1  # count n itself

        return result
        # Time: O(log n)  Space: O(log n)
# @lc code=end
