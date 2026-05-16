#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Monotonic deque: maintain indices of elements in DECREASING order of value
        # Front of deque always holds the index of the maximum in current window
        # Elements smaller than a new element are useless — they'll never be the max
        dq = deque()   # stores indices, values are decreasing front→back
        result = []

        for i in range(len(nums)):
            # Remove indices that are outside the window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove indices whose values are smaller than current — they're useless
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Window is full — record the maximum (front of deque)
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        # Time: O(n)  Space: O(k)
# @lc code=end
