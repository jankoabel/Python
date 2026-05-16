#
# @lc app=leetcode id=968 lang=python
#
# [968] Binary Tree Cameras (HARD)
#
# PROBLEM:
# Place cameras on some nodes so that every node is monitored.
# A camera monitors itself, its parent, and its children.
# Return minimum cameras needed.
# Example: root=[0,0,null,0,0] → 1
#
# APPROACH: Greedy DFS — post-order.
# Each node returns one of 3 states:
# 0 = not covered (parent must place camera)
# 1 = has camera
# 2 = covered (no camera needed here)
# Greedily place cameras at lowest level needed.

# @lc code=start
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cameras = 0

        def dfs(node):
            if not node:
                return 2  # null nodes are "covered" (don't need camera)

            left  = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                # At least one child is uncovered — must place camera here
                self.cameras += 1
                return 1

            if left == 1 or right == 1:
                # At least one child has camera — this node is covered
                return 2

            # Both children are covered (state 2) — this node is uncovered
            return 0

        if dfs(root) == 0:
            # Root itself is uncovered — place camera there
            self.cameras += 1

        return self.cameras
        # Time: O(n)  Space: O(h)
# @lc code=end
