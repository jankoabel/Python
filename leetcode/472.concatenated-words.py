#
# @lc app=leetcode id=472 lang=python
#
# [472] Concatenated Words (HARD)
#
# PROBLEM:
# Given an array of strings words, return all concatenated words —
# words that can be formed by concatenating two or more shorter words from the array.
# Example: words=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#          → ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# APPROACH: Build a word set. For each word, use DP (word break) to check if
# it can be formed by at least 2 other words.

# @lc code=start
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_set = set(words)

        def can_form(word):
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    # dp[j] must be valid AND the substring j..i must be a different word
                    if dp[j] and word[j:i] in word_set and (j > 0 or i < n):
                        dp[i] = True
                        break
            return dp[n]

        return [w for w in words if can_form(w)]
        # Time: O(n * L^2)  Space: O(n)
# @lc code=end
