#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # Use the already-connected 'next' pointers to traverse each level
        # This is O(1) extra space (no queue needed for perfect binary tree)
        if not root:
            return root

        leftmost = root   # start of each level

        while leftmost.left:   # while there's a next level (perfect tree: left exists iff right exists)
            curr = leftmost
            while curr:
                # Connect left child to right child (same parent)
                curr.left.next = curr.right

                # Connect right child to left child of next node in same level
                if curr.next:
                    curr.right.next = curr.next.left

                curr = curr.next   # move right along current level

            leftmost = leftmost.left   # move down one level

        return root
        # Time: O(n)  Space: O(1)
# @lc code=end
