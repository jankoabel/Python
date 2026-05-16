#
# @lc app=leetcode id=854 lang=python
#
# [854] K-Similar Strings (HARD)
#
# PROBLEM:
# Strings s1 and s2 are k-similar if you can swap two adjacent letters in s1
# at most k times to make them equal. Return minimum k.
# Example: s1="ab", s2="ba" → 1  ;  s1="abc", s2="bca" → 2
#
# APPROACH: BFS on states (string configurations).
# Find the first mismatched position, try all swaps that fix it,
# and BFS for shortest path.

# @lc code=start
from collections import deque

class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        queue = deque([(s1, 0)])
        visited = {s1}

        while queue:
            curr, steps = queue.popleft()
            if curr == s2:
                return steps

            # Find first mismatch
            i = 0
            while curr[i] == s2[i]:
                i += 1

            # Try swapping position i with any j > i where curr[j] == s2[i]
            curr = list(curr)
            for j in range(i + 1, len(curr)):
                if curr[j] == s2[i]:
                    curr[i], curr[j] = curr[j], curr[i]
                    nxt = ''.join(curr)
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
                    curr[i], curr[j] = curr[j], curr[i]  # undo swap

        return -1
        # Time: O(n! / pruning)  Space: O(n! states)
# @lc code=end
