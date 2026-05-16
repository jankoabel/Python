#
# @lc app=leetcode id=1696 lang=python
#
# [1696] Jump Game VI
#
# PROBLEM:
# You are at index 0 of array nums. Each step, jump forward 1 to k positions.
# Collect nums[i] along the way. Return maximum score reaching the last index.
# Example: nums=[1,-1,-2,4,-7,3], k=2 → 7 (1 → -1 → 4 → 3)
#
# APPROACH: DP + monotonic deque for sliding window maximum.
# dp[i] = max score to reach index i.
# dp[i] = nums[i] + max(dp[i-k..i-1]).
# Use a deque to maintain max of last k dp values in O(1).

# @lc code=start
from collections import deque

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque([0])  # indices, decreasing by dp value

        for i in range(1, n):
            # Remove elements outside window
            while dq and dq[0] < i - k:
                dq.popleft()
            dp[i] = nums[i] + dp[dq[0]]
            # Maintain decreasing deque
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return dp[n-1]
        # Time: O(n)  Space: O(n)
# @lc code=end
