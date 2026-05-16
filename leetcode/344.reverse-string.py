#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#
# PROBLEM:
# Write a function that reverses a character array in-place.
# Must use O(1) extra space.
# Example: ["h","e","l","l","o"] → ["o","l","l","e","h"]

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None
        """
        # Classic two-pointer swap from both ends toward center
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # Time: O(n)  Space: O(1)
# @lc code=end
