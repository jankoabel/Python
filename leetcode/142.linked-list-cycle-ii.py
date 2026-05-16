#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# PROBLEM:
# Given the head of a linked list, return the node where the cycle begins.
# If no cycle, return null. Do not modify the list.
#
# APPROACH: Floyd's algorithm in two phases.
# Phase 1: Find where slow and fast meet (inside the cycle).
# Phase 2: Reset one pointer to head. Move both one step at a time.
#          They meet at the CYCLE ENTRANCE.
# Math proof: distance from head to entrance = distance from meeting point to entrance.

# @lc code=start
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        # Phase 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None   # no cycle

        # Phase 2: find cycle entrance
        slow = head          # reset one pointer to head
        while slow != fast:
            slow = slow.next
            fast = fast.next  # both move 1 step now

        return slow   # meeting point = cycle entrance
        # Time: O(n)  Space: O(1)
# @lc code=end
