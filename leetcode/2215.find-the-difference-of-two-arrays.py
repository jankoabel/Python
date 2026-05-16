#
# @lc app=leetcode id=2215 lang=python
#
# [2215] Find the Difference of Two Arrays
#
# PROBLEM:
# Given nums1 and nums2, return a list of two arrays:
# answer[0] = distinct values in nums1 not in nums2
# answer[1] = distinct values in nums2 not in nums1
# Example: nums1=[1,2,3], nums2=[2,4,6] → [[1,3],[4,6]]
#
# APPROACH: Convert to sets, use set difference.

# @lc code=start
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
        # Time: O(m+n)  Space: O(m+n)
# @lc code=end
