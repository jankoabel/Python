#
# @lc app=leetcode id=2130 lang=python
#
# [2130] Maximum Twin Sum of a Linked List
#
# PROBLEM:
# In a linked list of even length n, node i and node (n-1-i) are twins.
# Return the maximum twin sum.
# Example: [5,4,2,1] → 6 (5+1=6 or 4+2=6)
#
# APPROACH: Find middle, reverse second half, walk both halves summing twins.

# @lc code=start
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half starting at slow
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Compare from both ends
        left, right = head, prev
        best = 0
        while right:
            best = max(best, left.val + right.val)
            left = left.next
            right = right.next

        return best
        # Time: O(n)  Space: O(1)
# @lc code=end
