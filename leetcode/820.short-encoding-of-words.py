#
# @lc app=leetcode id=820 lang=python
#
# [820] Short Encoding of Words
#
# PROBLEM:
# A valid encoding of words is a reference string s and indices[] such that
# for each word, it is a suffix of s[indices[i]..] ending with '#'.
# Return the length of the shortest reference string s.
# Example: words=["time","me","bell"] → 10 ("time#bell#")
#
# APPROACH: A word doesn't need its own slot if it is a suffix of another word.
# Use a set of all words. For each word, remove all its proper suffixes.
# Remaining words in the set each need (len+1) characters (word + '#').

# @lc code=start
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_set = set(words)
        for word in words:
            # Remove all proper suffixes of this word
            for k in range(1, len(word)):
                word_set.discard(word[k:])
        return sum(len(w) + 1 for w in word_set)
        # Time: O(sum of word lengths squared)  Space: O(n)
# @lc code=end
