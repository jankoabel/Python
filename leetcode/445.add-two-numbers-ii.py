#
# @lc app=leetcode id=445 lang=python
#
# [445] Add Two Numbers II
#
# PROBLEM:
# Two non-empty linked lists represent two non-negative integers stored
# in forward order (most significant digit first). Add the two numbers.
# Example: (7→2→4→3) + (5→6→4) → 7→8→0→7
#
# APPROACH: Use two stacks to reverse the digit order.
# Pop from both stacks, add with carry, prepend result nodes.

# @lc code=start
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        while l1:
            s1.append(l1.val); l1 = l1.next
        while l2:
            s2.append(l2.val); l2 = l2.next

        carry = 0
        head = None
        while s1 or s2 or carry:
            val = carry
            if s1: val += s1.pop()
            if s2: val += s2.pop()
            carry, digit = divmod(val, 10)
            # Prepend new node
            node = ListNode(digit)
            node.next = head
            head = node

        return head
        # Time: O(m+n)  Space: O(m+n)
# @lc code=end
