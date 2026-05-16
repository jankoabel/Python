#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            for start, end in [(i, i), (i, i + 1)]:
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    if end - start + 1 > len(result):
                        result = s[start:end + 1]
                    start -= 1
                    end += 1
        return result
# @lc code=end
