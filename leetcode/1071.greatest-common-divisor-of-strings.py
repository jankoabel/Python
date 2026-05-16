#
# @lc app=leetcode id=1071 lang=python
#
# [1071] Greatest Common Divisor of Strings
#
# PROBLEM:
# For two strings s and t, t divides s if s = t + t + ... + t.
# Return the largest string that divides both str1 and str2.
# Example: str1="ABCABC", str2="ABC" → "ABC"
#
# APPROACH: If a GCD string exists, str1+str2 == str2+str1.
# The length of the GCD string is gcd(len(str1), len(str2)).

# @lc code=start
from math import gcd

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Necessary condition: concatenation must be commutative
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]
        # Time: O(m+n)  Space: O(m+n) for string comparison
# @lc code=end
