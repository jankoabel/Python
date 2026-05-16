#
# @lc app=leetcode id=1657 lang=python
#
# [1657] Determine if Two Strings Are Close
#
# PROBLEM:
# Two strings are "close" if you can make one equal to the other using:
# Op1: Swap any two chars  Op2: Transform all occurrences of one char to another.
# Return true if word1 and word2 are close.
# Example: word1="abc", word2="bca" → True  ;  word1="a", word2="aa" → False
#
# APPROACH: Two strings are close iff:
# 1. They have the same set of distinct characters.
# 2. They have the same multiset of character frequencies.

# @lc code=start
from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1, c2 = Counter(word1), Counter(word2)
        # Same distinct characters AND same frequency multiset
        return set(c1.keys()) == set(c2.keys()) and \
               sorted(c1.values()) == sorted(c2.values())
        # Time: O(n log n)  Space: O(1) — at most 26 chars
# @lc code=end
