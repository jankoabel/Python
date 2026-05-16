#
# @lc app=leetcode id=1531 lang=python
#
# [1531] String Compression II (HARD)
#
# PROBLEM:
# Run-length encoding compresses "aabccc" to "a2bc3". Delete at most k characters
# to minimize the encoded length.
# Example: s="aaabcccd", k=2 → 4 (delete 'b','d' → "aaaccc" → "a3c3")
#
# APPROACH: DP with memoization.
# dp(i, last_char, last_count, k_remaining) = min encoded length from i onward.
# At each position: delete or keep the character.

# @lc code=start
from functools import lru_cache

class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def rle_len(count):
            if count == 0: return 0
            if count == 1: return 1
            return 1 + len(str(count))

        @lru_cache(maxsize=None)
        def dp(i, last, last_cnt, rem):
            if rem < 0:
                return float('inf')
            if i == len(s):
                return 0
            # Delete s[i]
            res = dp(i + 1, last, last_cnt, rem - 1)
            # Keep s[i]
            if s[i] == last:
                inc = 1 if last_cnt in (1, 9, 99) else 0
                res = min(res, inc + dp(i + 1, last, last_cnt + 1, rem))
            else:
                res = min(res, 1 + dp(i + 1, s[i], 1, rem))
            return res

        return dp(0, '', 0, k)
        # Time: O(n^2 * k)  Space: O(n^2 * k)
# @lc code=end
