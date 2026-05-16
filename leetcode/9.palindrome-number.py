#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers and numbers ending in 0 (except 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Reverse only the second half of the number
        # This avoids overflow and avoids converting to string
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even-length: x == reversed_half
        # For odd-length:  x == reversed_half // 10  (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10
        # Time: O(log x)  Space: O(1)
# @lc code=end
