#
# @lc app=leetcode id=1768 lang=python
#
# [1768] Merge Strings Alternately
#
# PROBLEM:
# Given two strings word1 and word2, merge them alternately, starting with word1.
# If one runs out, append the remainder of the other.
# Example: word1="abc", word2="pqr" → "apbqcr"
#          word1="ab",  word2="pqrs" → "apbqrs"
#
# APPROACH: Use zip to pair characters, then append leftovers.

# @lc code=start
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        for a, b in zip(word1, word2):
            result.append(a)
            result.append(b)
        # Append remaining characters from the longer string
        result.append(word1[len(word2):])
        result.append(word2[len(word1):])
        return ''.join(result)
        # Time: O(m+n)  Space: O(m+n)
# @lc code=end
