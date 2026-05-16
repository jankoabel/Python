#
# @lc app=leetcode id=233 lang=python
#
# [233] Number of Digit One (HARD)
#
# PROBLEM:
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers <= n.
# Example: n=13 → 6  ;  n=0 → 0
#
# APPROACH: Mathematical position analysis.
# For each digit position (ones, tens, hundreds, ...):
# Count how many times '1' appears at that position across 0..n.
# Formula uses higher digits (hi), current digit (cur), lower digits (lo).

# @lc code=start
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        factor = 1

        while factor <= n:
            hi  = n // (factor * 10)
            cur = (n // factor) % 10
            lo  = n % factor

            if cur == 0:
                count += hi * factor
            elif cur == 1:
                count += hi * factor + lo + 1
            else:
                count += (hi + 1) * factor

            factor *= 10

        return count
        # Time: O(log n)  Space: O(1)
# @lc code=end
