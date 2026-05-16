#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# PROBLEM:
# Given the root of a binary tree, check whether it is a mirror of itself
# (symmetric around its center).
# Example: [1,2,2,3,4,4,3] → True ;  [1,2,2,null,3,null,3] → False

# @lc code=start
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Check if left subtree is a mirror of right subtree
        def is_mirror(left, right):
            if not left and not right:
                return True     # both null: symmetric
            if not left or not right:
                return False    # one null, one not: asymmetric
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and   # outer pair
                    is_mirror(left.right, right.left))      # inner pair

        return is_mirror(root.left, root.right)
        # Time: O(n)  Space: O(h)
# @lc code=end
