#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]
# @lc code=end
