#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)
        missing = len(t)
        result = ""
        j = 0
        for i, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if missing == 0:
                while need[s[j]] < 0:
                    need[s[j]] += 1
                    j += 1
                window = s[j:i + 1]
                if not result or len(window) < len(result):
                    result = window
                need[s[j]] += 1
                missing += 1
                j += 1
        return result
# @lc code=end
