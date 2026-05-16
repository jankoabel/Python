#
# @lc app=leetcode id=1316 lang=python
#
# [1316] Distinct Echo Substrings (HARD)
#
# PROBLEM:
# Return the number of distinct non-empty substrings of text that can be
# written as a concatenation of some string with itself (t = s + s).
# Example: text="abcabcabc" → 3 ("abcabc", "bcabca", "cabcab")
#
# APPROACH: For each possible half-length L, check all positions i where
# text[i:i+L] == text[i+L:i+2L]. Use rolling hash for O(1) comparison.

# @lc code=start
class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        found = set()
        MOD = (1 << 61) - 1
        BASE = 31

        for L in range(1, n // 2 + 1):
            # Check all positions for echo substrings of half-length L
            h1 = h2 = 0
            power = pow(BASE, L - 1, MOD)

            # Initialize first two windows
            for i in range(L):
                h1 = (h1 * BASE + ord(text[i]) - 96) % MOD
                h2 = (h2 * BASE + ord(text[i + L]) - 96) % MOD

            if h1 == h2 and text[:L] == text[L:2*L]:
                found.add(text[:2*L])

            for i in range(1, n - 2*L + 1):
                h1 = (h1 - (ord(text[i-1]) - 96) * power % MOD + MOD) % MOD
                h1 = (h1 * BASE + ord(text[i+L-1]) - 96) % MOD
                h2 = (h2 - (ord(text[i+L-1]) - 96) * power % MOD + MOD) % MOD
                h2 = (h2 * BASE + ord(text[i+2*L-1]) - 96) % MOD
                if h1 == h2:
                    s = text[i:i+2*L]
                    if text[i:i+L] == text[i+L:i+2*L]:
                        found.add(s)

        return len(found)
        # Time: O(n^2)  Space: O(n^2)
# @lc code=end
