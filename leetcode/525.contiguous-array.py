#
# @lc app=leetcode id=525 lang=python
#
# [525] Contiguous Array
#

# @lc code=start
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Replace 0s with -1, then find longest subarray with sum = 0
        # If prefix sum at index j equals prefix sum at index i (j > i),
        # then nums[i+1..j] has equal 0s and 1s
        prefix_sum = 0
        seen = {0: -1}   # prefix_sum → earliest index it appeared
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1   # treat 0 as -1

            if prefix_sum in seen:
                # Found same prefix sum before → subarray between is balanced
                max_len = max(max_len, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i   # record first occurrence

        return max_len
        # Time: O(n)  Space: O(n)
# @lc code=end
