#
# @lc app=leetcode id=2095 lang=python
#
# [2095] Delete the Middle Node of a Linked List
#
# PROBLEM:
# Given the head of a linked list, delete the middle node.
# The middle node of a list of size n is the ⌊n/2⌋th node (0-indexed).
# Example: [1,3,4,7,1,2,6] → [1,3,4,1,2,6]  (middle is node 4, index 3)
#
# APPROACH: Fast and slow pointers. Slow pointer trails one step behind
# (using a prev pointer). When fast reaches end, prev.next = prev.next.next.

# @lc code=start
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head.next.next  # start fast 2 ahead so slow lands just before middle
        prev = None

        # Actually use standard approach: slow lags by 1 using prev
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is now at middle, prev is one before it
        prev.next = slow.next
        return head
        # Time: O(n)  Space: O(1)
# @lc code=end
