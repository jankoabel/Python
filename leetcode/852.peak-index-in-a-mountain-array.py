#
# @lc app=leetcode id=852 lang=python
#
# [852] Peak Index in a Mountain Array
#
# PROBLEM:
# A mountain array strictly increases then strictly decreases.
# Return the index of the peak element.
# Example: arr=[0,1,0] → 1  ;  arr=[0,2,1,0] → 1
#
# APPROACH: Binary search. If arr[mid] < arr[mid+1], peak is to the right.
# Otherwise peak is at mid or to the left.

# @lc code=start
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1   # ascending side, peak is right
            else:
                hi = mid       # descending side, peak is here or left
        return lo
        # Time: O(log n)  Space: O(1)
# @lc code=end
