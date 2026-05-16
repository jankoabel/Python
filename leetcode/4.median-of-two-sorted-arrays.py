#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
# PROBLEM:
# Given two sorted arrays nums1 and nums2 of size m and n,
# return the median of the two sorted arrays.
# Must run in O(log(m+n)) time.
#
# APPROACH: Binary search on the smaller array.
# Partition both arrays so that:
#   left_half = first (m+n)//2 elements of combined sorted array
#   right_half = remaining elements
# Find the partition where max(left) <= min(right) on both sides.

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Always binary search on the SMALLER array for efficiency
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        left, right = 0, len(A) - 1

        while True:
            i = (left + right) // 2       # partition index in A (mid of A)
            j = half - i - 2              # partition index in B (computed from half)

            # Values just left and right of each partition
            A_left  = A[i] if i >= 0 else float('-inf')
            A_right = A[i+1] if i+1 < len(A) else float('inf')
            B_left  = B[j] if j >= 0 else float('-inf')
            B_right = B[j+1] if j+1 < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                # Found correct partition
                if total % 2 == 1:
                    return float(min(A_right, B_right))   # odd total: middle element
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                right = i - 1    # A's left side too large, move partition left
            else:
                left = i + 1     # A's left side too small, move partition right
        # Time: O(log(min(m,n)))  Space: O(1)
# @lc code=end
