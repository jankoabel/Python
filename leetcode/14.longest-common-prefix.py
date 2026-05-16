#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
# PROBLEM:
# Write a function to find the longest common prefix string among an array of strings.
# If no common prefix, return "".
# Example: ["flower","flow","flight"] → "fl"

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with first string as candidate prefix
        # Trim it until every other string starts with it
        prefix = strs[0]

        for s in strs[1:]:
            # Keep shrinking prefix until s starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
        # Time: O(S) where S = total characters  Space: O(1)
# @lc code=end
