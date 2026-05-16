#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#
# PROBLEM:
# Given an integer array, rotate it to the right by k steps.
# Example: [1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]
# Must solve with O(1) extra space.
#
# APPROACH: Three reverses trick.
# 1. Reverse the entire array
# 2. Reverse the first k elements
# 3. Reverse the remaining n-k elements
# Example: [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1] → [5,6,7,4,3,2,1] → [5,6,7,1,2,3,4]

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n = len(nums)
        k %= n   # k can be larger than n — normalize

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)    # step 1: reverse all
        reverse(0, k - 1)    # step 2: reverse first k
        reverse(k, n - 1)    # step 3: reverse the rest
        # Time: O(n)  Space: O(1)
# @lc code=end
