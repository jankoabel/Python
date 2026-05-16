#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two pointer approach — O(1) space
        # At each position, water level = min(max_left, max_right) - height[i]
        # We process the smaller side first because that side's water is determined
        left, right = 0, len(height) - 1
        max_left = max_right = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                # Left side is the limiting factor
                if height[left] >= max_left:
                    max_left = height[left]     # update max seen from left
                else:
                    water += max_left - height[left]  # this cell can hold water
                left += 1
            else:
                # Right side is the limiting factor
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1

        return water
        # Time: O(n)  Space: O(1)
# @lc code=end
