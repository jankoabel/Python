#
# @lc app=leetcode id=480 lang=python
#
# [480] Sliding Window Median (HARD)
#
# PROBLEM:
# Given an array nums and window size k, return the median of each window.
# Example: nums=[1,3,-1,-3,5,3,6,7], k=3 → [1,-1,-1,3,5,6]
#
# APPROACH: Two heaps (max-heap for lower half, min-heap for upper half).
# Use a lazy-deletion dict to mark removed elements.
# Balance heaps after each add/remove.

# @lc code=start
import heapq

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        lo = []  # max-heap (negate values)
        hi = []  # min-heap
        removed = {}  # value → count of lazily deleted elements

        # Initialize first window
        for num in nums[:k]:
            heapq.heappush(lo, -num)
        for _ in range(k // 2):
            heapq.heappush(hi, -heapq.heappop(lo))

        def get_median():
            if k % 2 == 1:
                return float(-lo[0])
            return (-lo[0] + hi[0]) / 2.0

        def balance():
            # Ensure len(lo) == len(hi) or len(lo) == len(hi) + 1
            while len(lo) - len(hi) > 1:
                heapq.heappush(hi, -heapq.heappop(lo))
            while len(hi) > len(lo):
                heapq.heappush(lo, -heapq.heappop(hi))

        def clean(heap, factor):
            # Remove lazily deleted elements from heap top
            while heap and removed.get(factor * heap[0], 0) > 0:
                removed[factor * heap[0]] -= 1
                heapq.heappop(heap)

        result = [get_median()]

        for i in range(k, len(nums)):
            out_val = nums[i - k]
            in_val  = nums[i]

            # Add incoming
            if in_val <= -lo[0]:
                heapq.heappush(lo, -in_val)
            else:
                heapq.heappush(hi, in_val)

            # Lazily mark outgoing
            removed[out_val] = removed.get(out_val, 0) + 1

            # Adjust sizes if out_val was in lo or hi
            if out_val <= -lo[0]:
                # Was in lo — size of lo effectively shrinks
                if in_val > -lo[0]:
                    pass  # already balanced
            else:
                pass  # similar

            # Clean tops and rebalance
            clean(lo, -1)
            clean(hi, 1)
            balance()
            clean(lo, -1)
            clean(hi, 1)

            result.append(get_median())

        return result
        # Time: O(n log k)  Space: O(n)
# @lc code=end
