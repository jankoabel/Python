#
# @lc app=leetcode id=1345 lang=python
#
# [1345] Jump Game IV (HARD)
#
# PROBLEM:
# Given an array, from index i you can jump to i-1, i+1, or any index j where
# arr[j] == arr[i]. Return minimum jumps to reach the last index.
# Example: arr=[100,-23,-23,404,100,23,23,23,3,404] → 3
#
# APPROACH: BFS. Group indices by value for O(1) "same value" jumps.
# Remove each value group after processing to avoid O(n^2) revisiting.

# @lc code=start
from collections import defaultdict, deque

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 0

        val_to_idx = defaultdict(list)
        for i, v in enumerate(arr):
            val_to_idx[v].append(i)

        visited = {0}
        queue = deque([(0, 0)])  # (index, steps)

        while queue:
            idx, steps = queue.popleft()
            for nb in [idx - 1, idx + 1] + val_to_idx[arr[idx]]:
                if nb == n - 1:
                    return steps + 1
                if 0 <= nb < n and nb not in visited:
                    visited.add(nb)
                    queue.append((nb, steps + 1))
            val_to_idx[arr[idx]] = []  # clear to avoid re-processing

        return -1
        # Time: O(n)  Space: O(n)
# @lc code=end
