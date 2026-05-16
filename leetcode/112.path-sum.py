#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# PROBLEM:
# Given the root of a binary tree and an integer targetSum,
# return true if there is a root-to-leaf path where the sum of node values equals targetSum.
# Example: root=[5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum=22 → True (5→4→11→2)

# @lc code=start
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        # Subtract current node's value from remaining target
        remaining = targetSum - root.val

        # Leaf node: check if remaining is zero
        if not root.left and not root.right:
            return remaining == 0

        # Recurse on children
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
        # Time: O(n)  Space: O(h)
# @lc code=end
