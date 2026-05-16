#
# @lc app=leetcode id=2458 lang=python
#
# [2458] Height of Binary Tree After Subtree Removal Queries (HARD)
#
# PROBLEM:
# Given a binary tree and queries[i]: remove the subtree rooted at queries[i]
# and return the height of the remaining tree.
# Example: root=[1,3,4,2,null,6,5,null,1], queries=[4] → [2]
#
# APPROACH: Precompute for each node: its depth and the maximum height
# achievable in the tree if this node's subtree were removed.
# Two DFS passes: one for depth/height, one for "best without me".

# @lc code=start
class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        # node -> (depth, height of subtree)
        depth = {}
        height = {}

        def dfs_down(node, d):
            if not node:
                return -1
            depth[node.val] = d
            h = max(dfs_down(node.left, d+1), dfs_down(node.right, d+1)) + 1
            height[node.val] = h
            return h

        dfs_down(root, 0)

        # answer[v] = max height of tree when node v is removed
        answer = {}

        def dfs_up(node, best_without):
            if not node:
                return
            answer[node.val] = best_without
            l, r = node.left, node.right
            lh = height[l.val] if l else -1
            rh = height[r.val] if r else -1
            # When going left, best is max(best_without, depth[node.val] + rh + 1)
            dfs_up(l, max(best_without, depth[node.val] + rh + 1))
            dfs_up(r, max(best_without, depth[node.val] + lh + 1))

        dfs_up(root, 0)

        return [answer[q] for q in queries]
        # Time: O(n + q)  Space: O(n)
# @lc code=end
