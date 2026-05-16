#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists (HARD)
#
# PROBLEM:
# Given an array of k sorted linked lists, merge them into one sorted list.
# Example: lists=[[1,4,5],[1,3,4],[2,6]] → [1,1,2,3,4,4,5,6]
#
# APPROACH: Min-heap of (value, list_index, node).
# Initialize with heads of all non-empty lists. Extract min, push next node.
# Use list_index as tiebreaker so ListNode isn't compared directly.

# @lc code=start
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = curr = ListNode(0)
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
        # Time: O(N log k) where N=total nodes  Space: O(k)
# @lc code=end
