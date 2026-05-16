#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Two pointer technique: 'write' pointer tracks where next unique element goes
        # 'read' pointer scans ahead looking for new values
        write = 1  # position to write next unique element (index 0 is always kept)

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:   # found a new unique value
                nums[write] = nums[read]        # place it at write position
                write += 1

        return write  # number of unique elements
        # Time: O(n)  Space: O(1)
# @lc code=end
