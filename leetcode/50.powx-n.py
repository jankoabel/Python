#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Fast exponentiation (binary exponentiation)
        # x^n = (x^2)^(n/2) if n is even
        #      = x * (x^2)^((n-1)/2) if n is odd
        # This reduces O(n) multiplications to O(log n)

        def power(x, n):
            if n == 0:
                return 1.0
            if n % 2 == 0:
                return power(x * x, n // 2)          # even: square and halve exponent
            return x * power(x * x, (n - 1) // 2)   # odd: multiply one x, then square

        if n < 0:
            x = 1 / x   # negative exponent → reciprocal
            n = -n

        return power(x, n)
        # Time: O(log n)  Space: O(log n) call stack
# @lc code=end
