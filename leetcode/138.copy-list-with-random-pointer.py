#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#
# PROBLEM:
# A linked list where each node has a 'next' pointer and a 'random' pointer
# (which can point to any node or null). Create a deep copy.
# Example: [[7,null],[13,0],[11,4],[10,2],[1,0]] → deep copy of same structure
#
# APPROACH: Hash map from original node → cloned node.
# Two passes: first create all clone nodes, then wire up next and random.

# @lc code=start
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        old_to_new = {}   # map: original node → its clone

        # First pass: create all clone nodes (values only)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: wire up next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
        # Time: O(n)  Space: O(n)
# @lc code=end
