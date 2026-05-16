#
# @lc app=leetcode id=2618 lang=python
#
# [2618] Check Whether Two Strings are Almost Equivalent
#
# PROBLEM:
# Two strings word1 and word2 are almost equivalent if the difference of
# frequency of each letter is at most 3.
# Example: word1="aaaa", word2="bccb" → False  ;  word1="abcdeef", word2="abaaacc" → True
#
# APPROACH: Count frequencies for both strings, check all 26 letters.

# @lc code=start
from collections import Counter

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        c1, c2 = Counter(word1), Counter(word2)
        for ch in set(c1) | set(c2):
            if abs(c1[ch] - c2[ch]) > 3:
                return False
        return True
        # Time: O(n)  Space: O(1)
# @lc code=end
