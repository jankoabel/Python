#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            for start, end in [(i, i), (i, i + 1)]:
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
        return count
# @lc code=end
