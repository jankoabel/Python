#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Sliding window of size len(s1) over s2
        # A permutation of s1 exists in s2 iff some window has the same char counts
        if len(s1) > len(s2):
            return False

        need = Counter(s1)    # character frequencies we need
        window = Counter()    # character frequencies in current window
        k = len(s1)

        for i, c in enumerate(s2):
            window[c] += 1                  # add right character

            if i >= k:
                # Remove leftmost character of outgoing window
                left = s2[i - k]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]

            if window == need:              # window is an anagram of s1
                return True

        return False
        # Time: O(len(s1) + len(s2))  Space: O(1) — at most 26 chars
# @lc code=end
