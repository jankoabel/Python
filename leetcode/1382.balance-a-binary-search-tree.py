#
# @lc app=leetcode id=1382 lang=python
#
# [1382] Balance a Binary Search Tree
#
# PROBLEM:
# Given the root of a BST, return a balanced BST with the same node values.
# A balanced BST has each node's subtree heights differing by at most 1.
#
# APPROACH:
# 1. In-order traversal → sorted array
# 2. Build balanced BST from sorted array by always picking the middle as root

# @lc code=start
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        vals = []

        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(vals[mid])
            node.left  = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        inorder(root)
        return build(0, len(vals) - 1)
        # Time: O(n)  Space: O(n)
# @lc code=end
