#
# @lc app=leetcode id=952 lang=python
#
# [952] Largest Component Size by Common Factor (HARD)
#
# PROBLEM:
# Given an integer array nums, build a graph where nums[i] and nums[j] are connected
# if they share a common factor > 1. Return the size of the largest connected component.
# Example: nums=[4,6,15,35] → 4
#
# APPROACH: Union-Find. For each number, factorize it and union the number with
# each of its prime factors (using factor as a "node").

# @lc code=start
class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        parent = list(range(max(nums) + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        for num in nums:
            d = 2
            n = num
            while d * d <= n:
                if n % d == 0:
                    union(num, d)
                    while n % d == 0:
                        n //= d
                d += 1
            if n > 1:
                union(num, n)

        count = {}
        best = 0
        for num in nums:
            root = find(num)
            count[root] = count.get(root, 0) + 1
            best = max(best, count[root])

        return best
        # Time: O(n * sqrt(max(nums)))  Space: O(max(nums))
# @lc code=end
