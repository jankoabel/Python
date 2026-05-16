#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        # Two pointers: 'write' tracks where the next non-zero goes
        # Walk 'read' through the array — whenever we see a non-zero,
        # place it at the write position. Zeros are left behind.
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]   # move non-zero forward
                write += 1

        # Fill the rest with zeros
        while write < len(nums):
            nums[write] = 0
            write += 1
        # Time: O(n)  Space: O(1)
# @lc code=end
