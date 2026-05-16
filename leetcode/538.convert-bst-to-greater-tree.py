#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#
# PROBLEM:
# Given the root of a BST, convert it to a Greater Sum Tree where every key
# is replaced with the sum of all keys greater than or equal to it.
# Example: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
#          → [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
# APPROACH: Reverse in-order traversal (right → root → left).
# Keep a running sum. Each node gets updated to running_sum + original value.

# @lc code=start
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.running_sum = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.running_sum += node.val
            node.val = self.running_sum
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
        # Time: O(n)  Space: O(h)
# @lc code=end
