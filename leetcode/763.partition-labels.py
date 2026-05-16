#
# @lc app=leetcode id=763 lang=python
#
# [763] Partition Labels
#
# PROBLEM:
# Partition string s into as many parts as possible so that each letter appears
# in at most one part. Return a list of the sizes of these parts.
# Example: s="ababcbacadefegdehijhklij" → [9,7,8]
#
# APPROACH: Greedy.
# Record the last occurrence of each character.
# Sweep through, tracking the furthest last-occurrence seen so far (max_end).
# When i == max_end, we've found a partition boundary.

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(s)}  # last occurrence of each char

        result = []
        start = max_end = 0

        for i, c in enumerate(s):
            max_end = max(max_end, last[c])
            if i == max_end:
                result.append(i - start + 1)
                start = i + 1

        return result
        # Time: O(n)  Space: O(1) — at most 26 chars
# @lc code=end
