#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Backtracking: try every possible first partition, recurse on the rest
        # Only continue if the chosen prefix is a palindrome
        result = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, current):
            if start == len(s):              # used entire string — valid partition
                result.append(list(current))
                return
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):    # only branch on palindrome prefixes
                    current.append(prefix)
                    backtrack(end, current)
                    current.pop()

        backtrack(0, [])
        return result
        # Time: O(2^n * n)  Space: O(n)
# @lc code=end
