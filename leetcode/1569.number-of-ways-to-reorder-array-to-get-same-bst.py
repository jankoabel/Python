#
# @lc app=leetcode id=1569 lang=python
#
# [1569] Number of Ways to Reorder Array to Get Same BST (HARD)
#
# PROBLEM:
# Given nums (a permutation of 1..n), count the number of different orderings
# of nums that produce the same BST structure as the original.
# Return count modulo 10^9 + 7.
# Example: nums=[2,1,3] → 1  ;  nums=[3,4,5,1,2] → 5
#
# APPROACH: Recursive with combinatorics.
# Root is always nums[0]. Left subtree = values < root, right = values > root.
# The relative order within left and right must be preserved.
# Ways = C(len(left)+len(right), len(left)) * ways(left) * ways(right)

# @lc code=start
from math import comb

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def count_ways(arr):
            if len(arr) <= 1:
                return 1
            root = arr[0]
            left  = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            # Choose positions for left subtree elements among (len(left)+len(right)) slots
            return comb(len(left) + len(right), len(left)) * count_ways(left) % MOD * count_ways(right) % MOD

        return (count_ways(nums) - 1) % MOD
        # Time: O(n^2)  Space: O(n^2)
# @lc code=end
