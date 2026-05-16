#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#
# PROBLEM:
# Given the root of a BST and a target integer k, return true if there exist
# two elements that sum to k.
# Example: root=[5,3,6,2,4,null,7], k=9 → True (2+7 or 3+6)
#
# APPROACH: In-order traversal to get sorted array, then two-pointer.
# Or: DFS + hash set (check if k - node.val has been seen).

# @lc code=start
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        seen = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        # Time: O(n)  Space: O(n)
# @lc code=end
