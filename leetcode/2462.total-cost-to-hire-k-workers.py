#
# @lc app=leetcode id=2462 lang=python
#
# [2462] Total Cost to Hire K Workers
#
# PROBLEM:
# Given costs[] of n workers, hire k workers in k rounds.
# Each round, from the first candidates or last candidates not yet hired,
# pick the cheapest (ties: smaller index). Return total cost.
# Example: costs=[17,12,10,2,7,2,11,20,8], k=3, candidates=4 → 11
#
# APPROACH: Two min-heaps — one for left window, one for right window.
# Advance the appropriate window pointer after each pick.

# @lc code=start
import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        n = len(costs)
        left_heap  = []  # (cost, index) for left candidates
        right_heap = []  # (cost, index) for right candidates

        left, right = 0, n - 1

        # Seed both heaps
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap,  (costs[left],  left))
                left += 1
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

        total = 0
        for _ in range(k):
            lv = left_heap[0]  if left_heap  else (float('inf'), -1)
            rv = right_heap[0] if right_heap else (float('inf'), -1)
            if lv[0] <= rv[0]:
                cost, _ = heapq.heappop(left_heap)
                total += cost
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                cost, _ = heapq.heappop(right_heap)
                total += cost
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        return total
        # Time: O((k + candidates) log candidates)  Space: O(candidates)
# @lc code=end
