#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#
# PROBLEM:
# Given the head of a linked list, return true if it is a palindrome.
# Must run in O(n) time and O(1) extra space.
# Example: [1,2,2,1] → True  ;  [1,2] → False
#
# APPROACH:
# 1. Find middle with slow/fast pointers.
# 2. Reverse the second half.
# 3. Compare first half with reversed second half.
# 4. (Optional) restore the list.

# @lc code=start
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Step 1: Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        second_half = prev   # head of reversed second half

        # Step 3: Compare
        first, second = head, second_half
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
        # Time: O(n)  Space: O(1)
# @lc code=end
