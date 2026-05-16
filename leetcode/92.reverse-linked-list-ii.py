#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#
# PROBLEM:
# Given the head of a linked list and two integers left and right,
# reverse the nodes from position left to right (1-indexed).
# Example: 1→2→3→4→5, left=2, right=4 → 1→4→3→2→5
#
# APPROACH: One pass. Find the node just before 'left', then
# repeatedly move the next node to front of the reversed section.

# @lc code=start
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prev = dummy

        # Move prev to the node just before position 'left'
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next   # first node of the section to reverse

        # Repeatedly take curr.next and insert it right after prev
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next       # unlink next_node
            next_node.next = prev.next       # point next_node to front of reversed section
            prev.next = next_node            # insert next_node at front

        return dummy.next
        # Time: O(n)  Space: O(1)
# @lc code=end
