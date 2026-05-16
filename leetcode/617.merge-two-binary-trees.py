#
# @lc app=leetcode id=617 lang=python
#
# [617] Merge Two Binary Trees
#
# PROBLEM:
# Merge two binary trees by overlapping them. Overlapping nodes sum their values;
# null nodes use the non-null node as-is.
# Example: tree1=[1,3,2,5], tree2=[2,1,3,null,4,null,7]
#          → [3,4,5,5,4,null,7]
#
# APPROACH: Recursive DFS — if both nodes exist, sum and recurse on children.
# If one is null, return the other.

# @lc code=start
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1
        # Both exist: merge in-place into root1
        root1.val += root2.val
        root1.left  = self.mergeTrees(root1.left,  root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
        # Time: O(min(m,n))  Space: O(min(h1,h2))
# @lc code=end
