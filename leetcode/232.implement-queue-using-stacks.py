#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#
# PROBLEM:
# Implement a FIFO queue using only two stacks.
# Implement push(x), pop(), peek(), empty().
# pop and peek must be amortized O(1).
#
# APPROACH: Two stacks — inbox and outbox.
# push → inbox. pop/peek → if outbox empty, pour ALL of inbox into outbox (reverses order).
# Each element is moved at most twice → amortized O(1).

# @lc code=start
class MyQueue(object):
    def __init__(self):
        self.inbox = []    # new elements pushed here
        self.outbox = []   # elements ready to be dequeued

    def push(self, x):
        self.inbox.append(x)

    def _transfer(self):
        if not self.outbox:   # only transfer when outbox is empty
            while self.inbox:
                self.outbox.append(self.inbox.pop())   # reverses order = queue order

    def pop(self):
        self._transfer()
        return self.outbox.pop()

    def peek(self):
        self._transfer()
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox
    # Amortized O(1) per operation
# @lc code=end
