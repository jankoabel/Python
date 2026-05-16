#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Classic binary search on a sorted array
        # Each step eliminates half the search space
        # Invariant: if target exists, it is within [left, right]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2   # avoid overflow (Python ints don't overflow but good habit)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1    # target is in the RIGHT half
            else:
                right = mid - 1   # target is in the LEFT half

        return -1   # not found
        # Time: O(log n)  Space: O(1)
# @lc code=end
