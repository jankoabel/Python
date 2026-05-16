#
# @lc app=leetcode id=700 lang=python
#
# [700] Search in a Binary Search Tree
#
# PROBLEM:
# Given the root of a BST and an integer val, find and return the subtree
# rooted with that node. Return null if not found.
# Example: root=[4,2,7,1,3], val=2 → [2,1,3]
#
# APPROACH: Iterative BST search — go left if val < node, right if val > node.

# @lc code=start
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root
        while node:
            if val == node.val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return None
        # Time: O(h)  Space: O(1)
# @lc code=end
