#
# @lc app=leetcode id=946 lang=python
#
# [946] Validate Stack Sequences
#
# PROBLEM:
# Given two integer arrays pushed and popped, return true if they could be
# the result of a sequence of push and pop operations on an initially empty stack.
# Example: pushed=[1,2,3,4,5], popped=[4,5,3,2,1] → True
#
# APPROACH: Simulate with a real stack.
# Push elements one by one. After each push, pop while stack top == next to pop.

# @lc code=start
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pop_idx = 0

        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1

        return len(stack) == 0
        # Time: O(n)  Space: O(n)
# @lc code=end
