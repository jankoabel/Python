#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#
# PROBLEM:
# Given an integer array sorted in ascending order, convert it to a
# height-balanced BST (|height(left) - height(right)| <= 1 for every node).
# Example: [-10,-3,0,5,9] → [0,-3,9,-10,null,5] (balanced BST)
#
# APPROACH: Recursively pick the MIDDLE element as root.
# This guarantees equal-size left and right subtrees → balanced.

# @lc code=start
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2       # middle element becomes root
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)    # left half → left subtree
            root.right = build(mid + 1, right)  # right half → right subtree
            return root

        return build(0, len(nums) - 1)
        # Time: O(n)  Space: O(log n) call stack
# @lc code=end
