#
# @lc app=leetcode id=1679 lang=python
#
# [1679] Max Number of K-Sum Pairs
#
# PROBLEM:
# Given an integer array nums and an integer k, in one operation pick two numbers
# that sum to k and remove them. Return max number of such operations.
# Example: nums=[1,2,3,4], k=5 → 2  ;  nums=[3,1,3,4,3], k=6 → 1
#
# APPROACH: Sort then two-pointer.
# Left+right pointers: if sum==k → count, move both; if sum<k → left++; else right--.

# @lc code=start
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            s = nums[left] + nums[right]
            if s == k:
                count += 1
                left += 1
                right -= 1
            elif s < k:
                left += 1
            else:
                right -= 1
        return count
        # Time: O(n log n)  Space: O(1)
# @lc code=end
