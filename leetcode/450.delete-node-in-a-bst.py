#
# @lc app=leetcode id=450 lang=python
#
# [450] Delete Node in a BST
#
# PROBLEM:
# Given a BST root and a key, delete the node with that key and return the root.
# Example: root=[5,3,6,2,4,null,7], key=3 → [5,4,6,2,null,null,7]
#
# APPROACH: Three cases:
# 1. Node has no right child → return left child
# 2. Node has no left child → return right child
# 3. Node has both → find in-order successor (leftmost in right subtree),
#    replace node's value with successor's value, delete successor from right subtree

# @lc code=start
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # Find in-order successor (min of right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root
        # Time: O(h)  Space: O(h)
# @lc code=end
