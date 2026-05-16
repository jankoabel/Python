#
# @lc app=leetcode id=2306 lang=python
#
# [2306] Naming a Company (HARD)
#
# PROBLEM:
# Given ideas (strings), swap first letters of any two ideas to form a company name.
# Count distinct company names: (A with swapped B's first letter) + (B with A's first letter)
# where neither result is in the original ideas set.
# Example: ideas=["coffee","donuts","time","toffee"] → 6
#
# APPROACH: Group ideas by their suffix (everything after first letter).
# For each pair of first letters (a, b), count suffixes that appear in a's group
# but not b's (and vice versa). Contribution = 2 * count_a_only * count_b_only.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        suffix_to_letters = defaultdict(set)
        for idea in ideas:
            suffix_to_letters[idea[1:]].add(idea[0])

        # Group suffixes by which first letters they appear with
        letter_to_suffixes = defaultdict(set)
        for suffix, letters in suffix_to_letters.items():
            for letter in letters:
                letter_to_suffixes[letter].add(suffix)

        result = 0
        letters = list(letter_to_suffixes.keys())
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                a, b = letters[i], letters[j]
                shared = len(letter_to_suffixes[a] & letter_to_suffixes[b])
                only_a = len(letter_to_suffixes[a]) - shared
                only_b = len(letter_to_suffixes[b]) - shared
                result += 2 * only_a * only_b

        return result
        # Time: O(n * 26^2)  Space: O(n)
# @lc code=end
