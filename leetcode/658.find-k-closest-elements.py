#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#
# PROBLEM:
# Given a sorted integer array arr, two integers k and x,
# return the k closest integers to x in arr, sorted in ascending order.
# Ties broken by smaller value.
# Example: arr=[1,2,3,4,5], k=4, x=3 → [1,2,3,4]
#
# APPROACH: Binary search for the left boundary of the window of size k.
# We want arr[mid..mid+k-1]. Compare distance of arr[mid] vs arr[mid+k] from x.
# If arr[mid] is further, slide window right.

# @lc code=start
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = (lo + hi) // 2
            # Compare left candidate vs right candidate of window
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1   # left end too far, slide right
            else:
                hi = mid

        return arr[lo:lo + k]
        # Time: O(log(n-k) + k)  Space: O(1)
# @lc code=end
