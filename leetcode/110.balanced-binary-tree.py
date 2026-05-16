#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# PROBLEM:
# Given a binary tree, determine if it is height-balanced:
# for every node, the height difference between left and right subtrees <= 1.
# Example: [3,9,20,null,null,15,7] → True ;  [1,2,2,3,3,null,null,4,4] → False
#
# APPROACH: Post-order DFS — return -1 as a sentinel for "unbalanced".
# This avoids computing height twice and runs in O(n).

# @lc code=start
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1    # already unbalanced in left subtree

            right = height(node.right)
            if right == -1:
                return -1    # already unbalanced in right subtree

            if abs(left - right) > 1:
                return -1    # THIS node is unbalanced

            return 1 + max(left, right)   # normal height

        return height(root) != -1
        # Time: O(n)  Space: O(h)
# @lc code=end
