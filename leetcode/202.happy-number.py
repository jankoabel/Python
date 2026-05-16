#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#
# PROBLEM:
# A happy number: repeatedly replace the number with the sum of squares of its digits.
# Eventually reaches 1 (happy) or loops forever (not happy).
# Example: 19 → 1^2 + 9^2 = 82 → 8^2+2^2 = 68 → ... → 1 (happy!)
#
# APPROACH: Floyd's cycle detection.
# If not happy, the sequence eventually cycles.
# Use slow/fast pointers on the sequence — if they meet at 1 → happy, else cycle.

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_num(x):
            total = 0
            while x:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        slow = n
        fast = next_num(n)   # fast starts one step ahead

        while fast != 1 and slow != fast:
            slow = next_num(slow)          # 1 step
            fast = next_num(next_num(fast)) # 2 steps

        return fast == 1   # if we stopped because fast==1, it's happy
        # Time: O(log n)  Space: O(1)
# @lc code=end
