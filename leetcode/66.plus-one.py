#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Walk from least significant digit (right to left)
        # If digit is < 9, just increment and done
        # If digit is 9, set to 0 and carry over to next digit
        # If all digits were 9 (e.g. [9,9,9]), we need a new leading 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits          # no carry, we're done
            digits[i] = 0             # digit was 9, becomes 0 with carry

        # All digits were 9 — prepend a 1
        return [1] + digits
        # Time: O(n)  Space: O(1)
# @lc code=end
