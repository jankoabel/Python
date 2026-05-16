#
# @lc app=leetcode id=328 lang=python
#
# [328] Odd Even Linked List
#
# PROBLEM:
# Given the head of a singly linked list, group all odd-indexed nodes together
# followed by even-indexed nodes. Indices are 1-based.
# Do this in O(1) extra space and O(n) time.
# Example: [1,2,3,4,5] → [1,3,5,2,4]
#
# APPROACH: Two separate chains — odd-indexed and even-indexed.
# Walk through connecting every other node, then join the two chains.

# @lc code=start
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd = head          # head of odd-indexed chain
        even = head.next    # head of even-indexed chain
        even_head = even    # save even head to connect at the end

        while even and even.next:
            odd.next = even.next     # skip even node
            odd = odd.next           # advance odd pointer

            even.next = odd.next     # skip odd node
            even = even.next         # advance even pointer

        odd.next = even_head   # connect end of odd chain to start of even chain
        return head
        # Time: O(n)  Space: O(1)
# @lc code=end
