#
# @lc app=leetcode id=646 lang=python
#
# [646] Maximum Length of Pair Chain
#
# PROBLEM:
# You are given n pairs [left, right]. A chain of pairs is formed when
# left_i > right_{i-1} for consecutive pairs.
# Return the length of the longest chain.
# Example: [[1,2],[2,3],[3,4]] → 2 ([1,2]→[3,4])
#
# APPROACH: Greedy (like interval scheduling).
# Sort pairs by their right endpoint. Greedily pick the pair that ends earliest
# and is compatible with the last picked pair.

# @lc code=start
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])  # sort by right endpoint
        count = 0
        cur_end = float('-inf')
        for left, right in pairs:
            if left > cur_end:
                count += 1
                cur_end = right
        return count
        # Time: O(n log n)  Space: O(1)
# @lc code=end
