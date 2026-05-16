#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Reduce to: can we pick a subset that sums to total/2?
        # This is a 0/1 knapsack problem
        total = sum(nums)
        if total % 2 != 0:
            return False    # odd total can't split evenly

        target = total // 2
        # dp[s] = True if sum s is achievable with a subset
        dp = {0}   # using a set of reachable sums (space-efficient)

        for num in nums:
            # Iterate in reverse to avoid using same element twice
            # Adding num to any currently reachable sum gives a new reachable sum
            dp = dp | {s + num for s in dp}
            if target in dp:
                return True

        return False
        # Time: O(n * target)  Space: O(target)
# @lc code=end
