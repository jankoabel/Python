#
# @lc app=leetcode id=1044 lang=python
#
# [1044] Longest Duplicate Substring (HARD)
#
# PROBLEM:
# Given string s, find the longest substring that occurs at least twice.
# Example: s="banana" → "ana"  ;  s="abcd" → ""
#
# APPROACH: Binary search on length + Rabin-Karp rolling hash.
# For a given length L, use rolling hash to check if any substring of length L
# appears more than once. Binary search for the largest such L.

# @lc code=start
class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        MOD = (1 << 61) - 1
        BASE = 31

        def check(L):
            if L == 0:
                return ""
            # Precompute hash for first window
            h = 0
            power = 1
            for i in range(L):
                h = (h * BASE + ord(s[i]) - ord('a') + 1) % MOD
                if i < L - 1:
                    power = power * BASE % MOD

            seen = {h: [0]}
            for i in range(1, len(s) - L + 1):
                h = (h - (ord(s[i-1]) - ord('a') + 1) * power % MOD + MOD) % MOD
                h = (h * BASE + ord(s[i+L-1]) - ord('a') + 1) % MOD
                if h in seen:
                    # Verify (hash collision possible)
                    for start in seen[h]:
                        if s[start:start+L] == s[i:i+L]:
                            return s[i:i+L]
                    seen[h].append(i)
                else:
                    seen[h] = [i]
            return None

        lo, hi = 0, len(s) - 1
        result = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            found = check(mid)
            if found is not None:
                result = found
                lo = mid + 1
            else:
                hi = mid - 1
        return result
        # Time: O(n log n)  Space: O(n)
# @lc code=end
