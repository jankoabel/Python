#
# @lc app=leetcode id=2629 lang=python
#
# [2629] Function Composition
#
# PROBLEM:
# Given an array of functions [f1, f2, ..., fn], return a composed function
# such that compose(x) = f1(f2(...fn(x))).
# If the array is empty, return the identity function.
# Example: fns=[x+1, x*x, x*2], x=4 → f1(f2(f3(4))) = (4*2)^2 +1 = 65
#
# APPROACH: Apply functions right to left using reduce or a loop.

# @lc code=start
class Solution(object):
    def compose(self, functions):
        """
        :type functions: List[Callable[[int], int]]
        :rtype: Callable[[int], int]
        """
        def composed(x):
            for f in reversed(functions):
                x = f(x)
            return x
        return composed
        # Time: O(n) per call  Space: O(1)
# @lc code=end
