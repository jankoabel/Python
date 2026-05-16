#
# @lc app=leetcode id=1032 lang=python
#
# [1032] Stream of Characters (HARD)
#
# PROBLEM:
# Design an algorithm that accepts a stream of characters and checks if any
# suffix of the characters seen so far matches any word in a given list.
# Example: words=["cd","f","kl"], stream=['a','b','c','d'] → [F,F,F,T] (at 'd', "cd" matches)
#
# APPROACH: Aho-Corasick automaton (or Trie + reverse matching).
# Simpler: Build a Trie on reversed words. Maintain a list of current Trie nodes.
# For each new char, advance all nodes one step. If any node is a word end → match.

# @lc code=start
class StreamChecker(object):

    def __init__(self, words):
        # Build Trie on reversed words
        self.trie = {}
        for word in words:
            node = self.trie
            for c in reversed(word):
                node = node.setdefault(c, {})
            node['#'] = True  # end of word marker

        self.stream = []  # recent characters (reversed)

    def query(self, letter):
        self.stream.append(letter)
        node = self.trie
        # Walk stream in reverse to match reversed words in trie
        for c in reversed(self.stream):
            if c not in node:
                return False
            node = node[c]
            if '#' in node:
                return True
        return False
        # Time: O(W*L) init, O(stream_len) per query  Space: O(W*L)
# @lc code=end
