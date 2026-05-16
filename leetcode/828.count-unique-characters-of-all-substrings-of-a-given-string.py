#
# @lc app=leetcode id=828 lang=python
#
# [828] Count Unique Characters of All Substrings of a Given String (HARD)
#
# PROBLEM:
# Let U(s) be the number of unique characters in s.
# Return sum of U(t) for all substrings t of s.
# Example: s="ABC" → 10  ;  s="ABA" → 8
#
# APPROACH: For each character at position i, count how many substrings have it
# as a unique occurrence. The contribution = (i - prev_same) * (next_same - i)
# where prev_same/next_same are positions of the previous/next same character.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # For each char, track last two positions seen
        last = defaultdict(lambda: [-1, -1])
        result = 0

        for i, c in enumerate(s):
            prev2, prev1 = last[c]
            # Contribution of s[i] = (i - prev1) * (next_i - i)
            # Since we process left to right, finalize contribution using prev2 and prev1
            result += (prev1 - prev2) * (i - prev1)
            last[c] = [prev1, i]

        # Finalize remaining
        n = len(s)
        for c, (prev2, prev1) in last.items():
            if prev1 != -1:
                result += (prev1 - prev2) * (n - prev1)

        return result
        # Time: O(n)  Space: O(1) — at most 26 chars
# @lc code=end
