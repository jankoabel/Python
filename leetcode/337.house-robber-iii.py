#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#
# PROBLEM:
# Houses are arranged in a binary tree. You cannot rob two directly linked houses.
# Find the maximum amount you can rob.
# Example: [3,2,3,null,3,null,1] → 7 (rob 3 + 3 + 1)
#
# APPROACH: Tree DP — for each node return a pair:
# (rob_this_node, skip_this_node)
# rob_this  = node.val + skip_left + skip_right
# skip_this = max(rob_left, skip_left) + max(rob_right, skip_right)

# @lc code=start
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)   # (rob_this, skip_this)

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # If we rob this node: can't rob children
            rob_this = node.val + left_skip + right_skip

            # If we skip this node: children can be robbed or not (take best)
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)

            return (rob_this, skip_this)

        return max(dfs(root))
        # Time: O(n)  Space: O(h)
# @lc code=end
