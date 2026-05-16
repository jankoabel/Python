#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#
# PROBLEM:
# Given a string s, return the number of palindromic substrings.
# Example: s="abc" → 3  ;  s="aaa" → 6
#
# APPROACH: Expand Around Center.
# For each center, expand outward while s[left]==s[right].
# Try both odd-length (i,i) and even-length (i,i+1) centers.

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            # Expand from each odd-length and even-length center
            for start, end in [(i, i), (i, i + 1)]:
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    count += 1
                    start -= 1
                    end += 1
        return count
        # Time: O(n^2)  Space: O(1)
# @lc code=end
