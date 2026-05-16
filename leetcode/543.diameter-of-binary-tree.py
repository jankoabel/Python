#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Diameter through a node = left_depth + right_depth
        # DFS: for each node, compute depth while updating the global max diameter
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # Diameter passing through this node = left + right edges
            self.max_diameter = max(self.max_diameter, left + right)
            # Return depth (longest path going DOWN from this node)
            return 1 + max(left, right)

        depth(root)
        return self.max_diameter
        # Time: O(n)  Space: O(h)
# @lc code=end
