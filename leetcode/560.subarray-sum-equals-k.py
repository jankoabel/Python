#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Prefix sum trick: sum(i..j) = prefix[j] - prefix[i-1]
        # We want prefix[j] - prefix[i-1] = k  →  prefix[i-1] = prefix[j] - k
        # Count how many times each prefix sum has occurred
        count = 0
        prefix_sum = 0
        seen = {0: 1}   # prefix_sum 0 has occurred once (before any element)

        for num in nums:
            prefix_sum += num
            # How many previous prefix sums equal (current - k)?
            # Each such occurrence means a valid subarray ending here
            count += seen.get(prefix_sum - k, 0)
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count
        # Time: O(n)  Space: O(n)
# @lc code=end
