#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#
# PROBLEM:
# Given n, return a list of strings 1..n where:
#   multiples of 3 → "Fizz"
#   multiples of 5 → "Buzz"
#   multiples of both → "FizzBuzz"
#   otherwise → the number as a string
# Example: n=15 → ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
        # Time: O(n)  Space: O(n)
# @lc code=end
