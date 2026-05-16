#
# @lc app=leetcode id=1372 lang=python
#
# [1372] Longest ZigZag Path in a Binary Tree
#
# PROBLEM:
# A ZigZag path alternates between left and right child moves.
# Return the length of the longest ZigZag path in the tree.
# Example: root=[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1] → 3
#
# APPROACH: DFS carrying (left_length, right_length) per node.
# left_length = max zigzag ending by going left from parent.
# right_length = max zigzag ending by going right from parent.

# @lc code=start
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 0

        def dfs(node, went_left, length):
            if not node:
                return
            self.best = max(self.best, length)
            if went_left:
                # Came from left: continue zigzag going right, or restart going left
                dfs(node.left,  True,  1)
                dfs(node.right, False, length + 1)
            else:
                dfs(node.left,  True,  length + 1)
                dfs(node.right, False, 1)

        dfs(root.left,  True,  1)
        dfs(root.right, False, 1)
        return self.best
        # Time: O(n)  Space: O(h)
# @lc code=end
