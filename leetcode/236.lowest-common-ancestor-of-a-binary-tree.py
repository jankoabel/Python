#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Post-order DFS: process children before parent
        # If we find p or q, return it upward
        # If both left and right subtrees return non-null → current node is LCA
        # If only one subtree returns non-null → propagate that upward
        if not root or root == p or root == q:
            return root   # base: found one of the targets or hit null

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root    # p is in one subtree, q is in the other → this is LCA
        return left or right   # one subtree has both, propagate upward
        # Time: O(n)  Space: O(n) call stack
# @lc code=end
