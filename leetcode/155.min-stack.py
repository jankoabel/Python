#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):
    def __init__(self):
        # Use two stacks: one for actual values, one to track running minimum
        # min_stack[i] stores the minimum of all values from bottom up to index i
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # New minimum is the smaller of val and the current minimum
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)   # first element is its own minimum

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()   # keep in sync

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]   # O(1) minimum lookup
        # All operations: Time O(1)  Space O(n)
# @lc code=end
