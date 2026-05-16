#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy BFS — treat each jump as a "level" in BFS
        # At each step, find the farthest we can reach from current range
        jumps = 0
        current_end = 0   # farthest index reachable with 'jumps' jumps
        farthest = 0      # farthest index reachable with 'jumps+1' jumps

        for i in range(len(nums) - 1):  # don't need to jump from last position
            farthest = max(farthest, i + nums[i])  # update max reach from i

            if i == current_end:         # we've exhausted current jump range
                jumps += 1               # must take another jump
                current_end = farthest   # new range is [current_end+1, farthest]

        return jumps
        # Time: O(n)  Space: O(1)
# @lc code=end
