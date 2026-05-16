#
# @lc app=leetcode id=2807 lang=python
#
# [2807] Insert Greatest Common Divisors in Linked List
#
# PROBLEM:
# Given the head of a linked list, between every pair of adjacent nodes insert
# a new node with value = gcd(node.val, node.next.val).
# Return the modified list.
# Example: [18,6,10,3] → [18,6,6,2,10,1,3]
#
# APPROACH: Walk the list. Between each pair, insert a GCD node.

# @lc code=start
from math import gcd

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            new_node = ListNode(g)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next  # skip the inserted node
        return head
        # Time: O(n)  Space: O(1)
# @lc code=end
