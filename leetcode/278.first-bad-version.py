#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#
# PROBLEM:
# You are a product manager. There are n versions [1..n].
# isBadVersion(v) returns whether version v is bad.
# All versions after a bad one are also bad.
# Find the first bad version using minimum number of API calls.
#
# APPROACH: Binary search — find the leftmost True in [F, F, ..., F, T, T, ..., T].

# @lc code=start
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid       # mid could be the first bad — don't exclude it
            else:
                left = mid + 1    # mid is good, first bad is strictly to the right

        return left   # left == right == first bad version
        # Time: O(log n)  Space: O(1)
# @lc code=end
