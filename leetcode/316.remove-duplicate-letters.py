#
# @lc app=leetcode id=316 lang=python
#
# [316] Remove Duplicate Letters
#
# PROBLEM:
# Given a string, remove duplicate letters so that every letter appears once,
# and return the smallest lexicographic result among all possible results.
# Example: "bcabc" → "abc"  ;  "cbacdcbc" → "acdb"
#
# APPROACH: Greedy with a monotonic stack.
# For each character: if it's smaller than the stack top AND the stack top appears
# later in the string (so we haven't "lost" it) → pop the stack top.
# This greedily builds the lexicographically smallest result.

# @lc code=start
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # last[c] = last index where character c appears
        last = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue   # already in result, skip

            # Pop larger characters if they appear later (we can add them back)
            while stack and c < stack[-1] and last[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)
        # Time: O(n)  Space: O(1) — at most 26 unique chars
# @lc code=end
