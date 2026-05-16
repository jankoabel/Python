#
# @lc app=leetcode id=906 lang=python
#
# [906] Super Palindromes (HARD)
#
# PROBLEM:
# A super-palindrome is a positive integer that is palindromic and also a perfect square.
# Given strings L and R (representing large integers), return how many super-palindromes
# exist in the range [L, R].
# Example: L="4", R="1000" → 4 (4,9,121,484)
#
# APPROACH: Generate palindromes (by mirroring digits) up to sqrt(R),
# square them, and check if the square is itself a palindrome.

# @lc code=start
class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        L, R = int(L), int(R)
        count = 0
        MAGIC = 100000  # sqrt(10^18) ~ 10^9, palindromes up to ~10^5

        # Odd-length palindromes: mirror around center
        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1]  # e.g. "123" → "12321"
            val = int(t) ** 2
            if val > R: break
            if val >= L and t == t[::-1]:
                count += 1

        # Even-length palindromes
        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1]   # e.g. "12" → "1221"
            val = int(t) ** 2
            if val > R: break
            if val >= L and t == t[::-1]:
                count += 1

        return count
        # Time: O(sqrt(R) * log(sqrt(R)))  Space: O(1)
# @lc code=end
