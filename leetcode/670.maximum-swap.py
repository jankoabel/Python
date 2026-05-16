#
# @lc app=leetcode id=670 lang=python
#
# [670] Maximum Swap
#
# PROBLEM:
# Given an integer num, you can swap two digits at most once to get the maximum.
# Return the maximum value you can get.
# Example: num=2736 → 7236  ;  num=9973 → 9973
#
# APPROACH: Record the last occurrence of each digit 0-9.
# For each digit from left to right, check if a larger digit exists later.
# Swap the first such pair found.

# @lc code=start
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}  # digit → last index

        for i, d in enumerate(digits):
            # Try largest possible digit that appears later
            for dig in range(9, int(d), -1):
                if last.get(dig, -1) > i:
                    # Swap digits[i] with digits[last[dig]]
                    j = last[dig]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))

        return num
        # Time: O(n)  Space: O(n)
# @lc code=end
