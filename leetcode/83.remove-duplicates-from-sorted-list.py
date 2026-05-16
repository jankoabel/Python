#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#
# PROBLEM:
# Given the head of a sorted linked list, delete all duplicates so each
# element appears only once. Return the modified list.
# Example: 1→1→2→3→3 → 1→2→3

# @lc code=start
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next   # skip the duplicate
            else:
                curr = curr.next             # move forward only if no duplicate
        return head
        # Time: O(n)  Space: O(1)
# @lc code=end
