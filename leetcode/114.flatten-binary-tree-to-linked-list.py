#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#
# PROBLEM:
# Given the root of a binary tree, flatten it to a linked list in-place
# using the right pointers (following pre-order traversal order).
# All left pointers should be set to null.
# Example: [1,2,5,3,4,null,6] → [1,null,2,null,3,null,4,null,5,null,6]
#
# APPROACH: Reverse pre-order (right, left, root) with a 'prev' pointer.
# Process right subtree first, then left, then connect root.right = prev.

# @lc code=start
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None
        """
        self.prev = None   # tracks the previously processed node

        def dfs(node):
            if not node:
                return
            dfs(node.right)    # process right first (reverse pre-order)
            dfs(node.left)
            node.right = self.prev   # connect current node to previously processed
            node.left = None         # clear left pointer
            self.prev = node         # this node is now the "previous"

        dfs(root)
        # Time: O(n)  Space: O(h)
# @lc code=end
