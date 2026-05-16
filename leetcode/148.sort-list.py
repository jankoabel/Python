#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
#
# PROBLEM:
# Given the head of a linked list, return the list sorted in ascending order.
# Must run in O(n log n) time and O(1) extra space (ignore recursion stack).
# Example: [4,2,1,3] → [1,2,3,4]
#
# APPROACH: Merge Sort on linked list.
# 1. Find midpoint with slow/fast pointers and split list in two.
# 2. Recursively sort each half.
# 3. Merge the two sorted halves.

# @lc code=start
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head   # base case: 0 or 1 nodes

        # Step 1: Find middle and split
        slow, fast = head, head.next   # fast starts 1 ahead to find left-mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None   # cut list in half

        # Step 2: Recursively sort
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge sorted halves
        dummy = curr = ListNode(0)
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right

        return dummy.next
        # Time: O(n log n)  Space: O(log n) recursion
# @lc code=end
