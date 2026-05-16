#
# @lc app=leetcode id=556 lang=python
#
# [556] Next Greater Element III
#
# PROBLEM:
# Given a positive integer n, find the smallest integer that uses the same digits
# and is greater than n. Return -1 if no such integer exists or exceeds 32-bit int.
# Example: n=12 → 21  ;  n=21 → -1
#
# APPROACH: "Next permutation" algorithm on the digits.
# 1. Find rightmost digit that is smaller than the digit to its right (pivot).
# 2. Swap pivot with the smallest digit to its right that is larger.
# 3. Reverse everything to the right of the pivot position.

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        k = len(digits)

        # Step 1: find pivot (rightmost i where digits[i] < digits[i+1])
        i = k - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1  # digits are descending — no next permutation

        # Step 2: find smallest digit to right of i that is > digits[i]
        j = k - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]

        # Step 3: reverse suffix after position i
        digits[i + 1:] = digits[i + 1:][::-1]

        result = int(''.join(digits))
        return result if result <= 2**31 - 1 else -1
        # Time: O(d) where d = number of digits  Space: O(d)
# @lc code=end
