#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# PROBLEM:
# Given the root of a binary tree, return the zigzag level order traversal:
# level 0 left→right, level 1 right→left, level 2 left→right, etc.
# Example: [3,9,20,null,null,15,7] → [[3],[20,9],[15,7]]

# @lc code=start
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True   # direction flag

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse alternate levels for zigzag effect
            result.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
