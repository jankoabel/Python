#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Floyd's cycle detection (tortoise and hare)
        # Treat the array as a linked list: index i points to nums[i]
        # Because one value is duplicated, there must be a cycle
        # Phase 1: find intersection point inside the cycle
        slow = fast = 0
        while True:
            slow = nums[slow]           # move 1 step
            fast = nums[nums[fast]]     # move 2 steps
            if slow == fast:
                break

        # Phase 2: find cycle entrance (= duplicate number)
        # Reset one pointer to start, keep other at intersection
        # Both move 1 step at a time → meet at cycle entrance
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        # Time: O(n)  Space: O(1) — no extra array or set needed
# @lc code=end
