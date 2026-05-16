#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group (HARD)
#
# PROBLEM:
# Given a linked list, reverse the nodes in groups of k. If remaining nodes < k,
# leave them as-is.
# Example: head=[1,2,3,4,5], k=2 → [2,1,4,3,5]
#
# APPROACH: Reverse k nodes at a time iteratively.
# Use a dummy head. For each group: check if k nodes remain, reverse the group,
# connect to previous tail and advance.

# @lc code=start
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if k nodes remain
            kth = self.get_kth(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            # Reverse k nodes
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect reversed group back
            tmp = group_prev.next    # old head (now new tail)
            group_prev.next = kth    # kth is new head
            tmp.next = group_next
            group_prev = tmp         # advance group_prev to new tail

        return dummy.next

    def get_kth(self, curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr
        # Time: O(n)  Space: O(1)
# @lc code=end
