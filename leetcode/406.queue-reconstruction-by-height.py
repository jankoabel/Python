#
# @lc app=leetcode id=406 lang=python
#
# [406] Queue Reconstruction by Height
#
# PROBLEM:
# You are given an array of people [h, k] where h is height and k is the number
# of people in front with height >= h. Reconstruct the queue.
# Example: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] → [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
#
# APPROACH: Greedy — sort by height descending (ties: k ascending).
# Insert each person at index k. Taller people are placed first,
# so inserting shorter people at index k is always valid.

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort tall-first; among same height, fewer-in-front first
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for person in people:
            result.insert(person[1], person)
        return result
        # Time: O(n^2) due to list insertion  Space: O(n)
# @lc code=end
