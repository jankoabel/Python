#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#

# @lc code=start
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS level by level — the LAST node at each level is visible from the right
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:     # last node in this level
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
