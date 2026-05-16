#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
# PROBLEM:
# Given a string of digits 2-9, return all possible letter combinations
# that the number could represent (like old T9 phone keyboards).
# 2→abc, 3→def, 4→ghi, 5→jkl, 6→mno, 7→pqrs, 8→tuv, 9→wxyz
# Example: "23" → ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
        }
        result = []

        def backtrack(i, current):
            if i == len(digits):        # used all digits → complete combination
                result.append(''.join(current))
                return
            for letter in phone[digits[i]]:
                current.append(letter)
                backtrack(i + 1, current)  # move to next digit
                current.pop()

        backtrack(0, [])
        return result
        # Time: O(4^n * n)  Space: O(n)
# @lc code=end
