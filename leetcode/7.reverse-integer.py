#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Handle negative numbers by working on absolute value, restore sign at end
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse digits by converting to string and flipping
        reversed_x = int(str(x)[::-1])

        # 32-bit signed integer range: [-2^31, 2^31 - 1]
        if reversed_x > 2**31 - 1:
            return 0

        return sign * reversed_x
        # Time: O(log x) — number of digits   Space: O(1)
# @lc code=end
