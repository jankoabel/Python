#
# @lc app=leetcode id=2390 lang=python
#
# [2390] Removing Stars From a String
#
# PROBLEM:
# Given a string s with stars '*', in one operation remove the star and the
# closest non-star character to its left. Return the resulting string.
# Example: s="leet**cod*e" → "lecoe"
#
# APPROACH: Use a stack. Push non-star chars. Pop when encountering a star.

# @lc code=start
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c == '*':
                stack.pop()   # remove closest non-star to the left
            else:
                stack.append(c)
        return ''.join(stack)
        # Time: O(n)  Space: O(n)
# @lc code=end
