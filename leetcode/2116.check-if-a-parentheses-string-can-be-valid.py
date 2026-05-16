#
# @lc app=leetcode id=2116 lang=python
#
# [2116] Check if a Parentheses String Can Be Valid
#
# PROBLEM:
# String s of '(' and ')'. locked[i]='0' means s[i] can be changed, '1' means locked.
# Return true if s can be a valid parentheses string.
# Example: s="()))()(", locked="010100" → True
#
# APPROACH: Two passes.
# Left-to-right: track min and max possible open count.
# If max < 0 at any point → impossible. At end, min must be 0.

# @lc code=start
class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 == 1:
            return False

        # Track range of possible open counts [lo, hi]
        lo = hi = 0
        for i in range(n):
            if locked[i] == '0':
                lo -= 1  # treat as ')'
                hi += 1  # treat as '('
            elif s[i] == '(':
                lo += 1
                hi += 1
            else:
                lo -= 1
                hi -= 1
            if hi < 0:
                return False
            lo = max(lo, 0)

        return lo == 0
        # Time: O(n)  Space: O(1)
# @lc code=end
