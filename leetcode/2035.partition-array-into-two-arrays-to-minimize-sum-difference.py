#
# @lc app=leetcode id=2035 lang=python
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference (HARD)
#
# PROBLEM:
# Split 2n numbers into two groups of n each to minimize |sum1 - sum2|.
# Example: nums=[3,9,7,3] → 2 (groups [3,9] sum=12 and [7,3] sum=10)
#
# APPROACH: Meet in the middle.
# Split array into two halves. For each half, compute all subset sums by size.
# For each subset of size k from left half, binary search in right half's size (n-k)
# subsets for best complement to make total_sum/2.

# @lc code=start
import bisect
from collections import defaultdict

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        total = sum(nums)
        left, right = nums[:n], nums[n:]

        def get_sums(arr):
            # Returns dict: size → sorted list of subset sums of that size
            res = defaultdict(list)
            for mask in range(1 << len(arr)):
                s = 0
                cnt = 0
                for i in range(len(arr)):
                    if mask >> i & 1:
                        s += arr[i]
                        cnt += 1
                res[cnt].append(s)
            for v in res.values():
                v.sort()
            return res

        left_sums  = get_sums(left)
        right_sums = get_sums(right)

        target = total / 2.0
        best = float('inf')

        for k in range(n + 1):
            for ls in left_sums[k]:
                rs_list = right_sums[n - k]
                # Binary search for best complement
                need = target - ls
                idx = bisect.bisect_left(rs_list, need)
                for i in [idx - 1, idx]:
                    if 0 <= i < len(rs_list):
                        diff = abs(total - 2 * (ls + rs_list[i]))
                        best = min(best, diff)

        return best
        # Time: O(2^n * n)  Space: O(2^n)
# @lc code=end
