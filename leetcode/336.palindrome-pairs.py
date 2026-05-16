#
# @lc app=leetcode id=336 lang=python
#
# [336] Palindrome Pairs (HARD)
#
# PROBLEM:
# Given a list of unique words, return all pairs [i,j] such that
# words[i] + words[j] is a palindrome.
# Example: words=["abcd","dcba","lls","s","sssll"] → [[0,1],[1,0],[3,2],[2,4]]
#
# APPROACH: Hash map word → index.
# For each word, split at every position and check if complement exists.
# Case 1: if left part is palindrome and reverse(right) is in map → (rev_right, i)
# Case 2: if right part is palindrome and reverse(left) is in map → (i, rev_left)

# @lc code=start
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(s):
            return s == s[::-1]

        word_map = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                left  = word[:j]
                right = word[j:]

                # Case 1: left is palindrome, look for reverse(right) at front
                if is_palindrome(left):
                    rev_right = right[::-1]
                    if rev_right != word and rev_right in word_map:
                        result.append([word_map[rev_right], i])

                # Case 2: right is palindrome, look for reverse(left) at back
                if j < n and is_palindrome(right):
                    rev_left = left[::-1]
                    if rev_left != word and rev_left in word_map:
                        result.append([i, word_map[rev_left]])

        return result
        # Time: O(n * k^2) where k = avg word length  Space: O(n)
# @lc code=end
