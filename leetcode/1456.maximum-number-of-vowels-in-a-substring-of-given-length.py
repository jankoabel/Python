#
# @lc app=leetcode id=1456 lang=python
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#
# PROBLEM:
# Given string s and integer k, return the maximum number of vowels
# in any substring of length k.
# Example: s="abciiidef", k=3 → 3 ("iii")
#
# APPROACH: Sliding window of size k. Count vowels. Slide and update count.

# @lc code=start
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        count = sum(1 for c in s[:k] if c in vowels)
        best = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            best = max(best, count)

        return best
        # Time: O(n)  Space: O(1)
# @lc code=end
