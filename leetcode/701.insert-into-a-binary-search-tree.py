#
# @lc app=leetcode id=701 lang=python
#
# [701] Insert into a Binary Search Tree
#
# PROBLEM:
# Given the root of a BST and an integer val, insert val into the BST.
# Return the root of the BST after insertion. Guaranteed val doesn't exist in tree.
# Example: root=[4,2,7,1,3], val=5 → [4,2,7,1,3,5]
#
# APPROACH: Follow BST property to find the correct null leaf position,
# then insert there.

# @lc code=start
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
        # Time: O(h)  Space: O(h)
# @lc code=end
