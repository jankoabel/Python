#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# PROBLEM:
# Given the root of a binary tree, return the inorder traversal (left, root, right).
# Example: [1,null,2,3] → [1,3,2]
#
# APPROACH: Iterative with a stack (avoids recursion limit).
# Push left children until null, then process node, then go right.

# @lc code=start
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()          # process this node (leftmost unprocessed)
            result.append(curr.val)
            curr = curr.right           # move to right subtree

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
