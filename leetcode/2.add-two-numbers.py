#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Simulate grade-school addition digit by digit
        # Both lists store digits in REVERSE order, so index 0 = ones place
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get digit values (0 if list is exhausted)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10          # carry into next digit
            digit = total % 10           # current digit

            curr.next = ListNode(digit)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
        # Time: O(max(m,n))  Space: O(max(m,n))
# @lc code=end
