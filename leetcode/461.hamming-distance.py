#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#
# PROBLEM:
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
# Example: x=1 (0001), y=4 (0100) → 2
#
# APPROACH: XOR x and y — result has 1s only where bits differ.
# Count the 1-bits (popcount).

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        count = 0
        while xor:
            count += xor & 1   # check lowest bit
            xor >>= 1
        return count
        # Alternatively: bin(x^y).count('1')
        # Time: O(1)  Space: O(1)
# @lc code=end
