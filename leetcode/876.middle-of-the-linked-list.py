#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#
# PROBLEM:
# Given the head of a singly linked list, return the middle node.
# If there are two middle nodes, return the second one.
# Example: [1,2,3,4,5] → node 3  ;  [1,2,3,4,5,6] → node 4
#
# APPROACH: Fast and slow pointers.
# Slow moves 1 step, fast moves 2 steps.
# When fast reaches the end, slow is at the middle.

# @lc code=start
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        # Time: O(n)  Space: O(1)
# @lc code=end
