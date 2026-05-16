#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#
# PROBLEM:
# nums1 is a subset of nums2. For each element in nums1, find the next greater
# element in nums2 (the first element to its right that is larger). Return -1 if none.
# Example: nums1=[4,1,2], nums2=[1,3,4,2] → [-1,3,-1]
#
# APPROACH: Monotonic stack on nums2.
# Process nums2 left to right. Maintain a decreasing stack.
# When we find a larger element, it is the "next greater" for everything in the stack.
# Build a map: value → next greater value. Then answer queries from nums1.

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []  # monotonic decreasing stack

        for num in nums2:
            # num is greater than stack top(s) — resolve them
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Anything remaining has no next greater
        for num in stack:
            next_greater[num] = -1

        return [next_greater[x] for x in nums1]
        # Time: O(m+n)  Space: O(n)
# @lc code=end
