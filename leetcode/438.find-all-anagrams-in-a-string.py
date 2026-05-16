#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Sliding window of size len(p) over s
        # Window is an anagram of p when its char counts match
        k = len(p)
        need = Counter(p)
        window = Counter(s[:k])   # initialize with first window
        result = []

        if window == need:
            result.append(0)

        for i in range(k, len(s)):
            # Add new right character
            window[s[i]] += 1

            # Remove leftmost character
            left = s[i - k]
            window[left] -= 1
            if window[left] == 0:
                del window[left]

            if window == need:
                result.append(i - k + 1)   # start index of this window

        return result
        # Time: O(n)  Space: O(1) — at most 26 unique chars
# @lc code=end
