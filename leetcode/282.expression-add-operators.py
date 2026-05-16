#
# @lc app=leetcode id=282 lang=python
#
# [282] Expression Add Operators (HARD)
#
# PROBLEM:
# Given a string of digits and a target, add operators +, -, * between digits
# so the expression evaluates to target. Return all such expressions.
# Example: num="123", target=6 → ["1+2+3","1*2*3"]
#
# APPROACH: Backtracking.
# Track: current expression string, current eval, and last multiplicand
# (needed to undo multiplication when we see another * after).

# @lc code=start
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []

        def backtrack(idx, path, value, last_mul):
            if idx == len(num):
                if value == target:
                    result.append(path)
                return
            for i in range(idx, len(num)):
                curr_str = num[idx:i+1]
                curr_val = int(curr_str)
                # Skip numbers with leading zeros
                if i > idx and num[idx] == '0':
                    break
                if idx == 0:
                    backtrack(i+1, curr_str, curr_val, curr_val)
                else:
                    backtrack(i+1, path+'+'+curr_str, value+curr_val, curr_val)
                    backtrack(i+1, path+'-'+curr_str, value-curr_val, -curr_val)
                    # For *, undo last addition and replace with product
                    backtrack(i+1, path+'*'+curr_str,
                              value - last_mul + last_mul * curr_val,
                              last_mul * curr_val)

        backtrack(0, "", 0, 0)
        return result
        # Time: O(4^n * n)  Space: O(n)
# @lc code=end
