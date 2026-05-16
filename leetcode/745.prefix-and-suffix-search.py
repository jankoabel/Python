#
# @lc app=leetcode id=745 lang=python
#
# [745] Prefix and Suffix Search (HARD)
#
# PROBLEM:
# Design a WordFilter class: given words[], implement f(pref, suff) which returns
# the index of the word with pref as prefix and suff as suffix (highest index wins).
# Return -1 if no such word.
# Example: WordFilter(["apple"]), f("a","e") → 0
#
# APPROACH: For each word, build all (suffix + "#" + prefix) → index mappings.
# On query, look up suff + "#" + pref.

# @lc code=start
class WordFilter(object):

    def __init__(self, words):
        self.lookup = {}
        for idx, word in enumerate(words):
            n = len(word)
            # Generate all suffix#prefix combinations
            for i in range(n + 1):
                suffix = word[i:]
                for j in range(n + 1):
                    prefix = word[:j]
                    self.lookup[suffix + '#' + prefix] = idx

    def f(self, pref, suff):
        return self.lookup.get(suff + '#' + pref, -1)
        # Time init: O(n * L^2)  Time query: O(L)  Space: O(n * L^2)
# @lc code=end
