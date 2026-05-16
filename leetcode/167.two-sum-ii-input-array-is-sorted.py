#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Because the array is SORTED, use two pointers from both ends
        # If sum > target → move right pointer left (reduce sum)
        # If sum < target → move left pointer right (increase sum)
        # Guaranteed to find a solution (problem states exactly one answer)
        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]   # 1-indexed answer
            elif s < target:
                left += 1    # need a larger sum
            else:
                right -= 1   # need a smaller sum
        # Time: O(n)  Space: O(1)
# @lc code=end
