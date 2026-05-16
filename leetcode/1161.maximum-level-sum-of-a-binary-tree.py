#
# @lc app=leetcode id=1161 lang=python
#
# [1161] Maximum Level Sum of a Binary Tree
#
# PROBLEM:
# Given the root of a binary tree, return the smallest level x such that
# the sum of all values at level x is maximal.
# Root is level 1.
# Example: root=[1,7,0,7,-8,null,null] → 2 (7+0=7 > 1)
#
# APPROACH: BFS level by level, compute sum at each level, track maximum.

# @lc code=start
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque([root])
        max_sum = float('-inf')
        best_level = level = 0

        while queue:
            level += 1
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                best_level = level

        return best_level
        # Time: O(n)  Space: O(w) where w = max width
# @lc code=end
