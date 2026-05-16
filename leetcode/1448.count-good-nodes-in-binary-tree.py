#
# @lc app=leetcode id=1448 lang=python
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS: carry the maximum value seen so far on the path from root
        # A node is "good" if its value >= max value on path from root to it
        def dfs(node, max_so_far):
            if not node:
                return 0

            # This node is good if it's >= all ancestors
            is_good = 1 if node.val >= max_so_far else 0

            # Update max for children
            new_max = max(max_so_far, node.val)

            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, float('-inf'))
        # Time: O(n)  Space: O(h) where h = tree height
# @lc code=end
