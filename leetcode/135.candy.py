#
# @lc app=leetcode id=135 lang=python
#
# [135] Candy (HARD)
#
# PROBLEM:
# n children in a row with ratings[]. Give each child at least 1 candy.
# Children with higher rating than neighbors must get more candy.
# Return minimum total candies.
# Example: ratings=[1,0,2] → 5  ;  ratings=[1,2,2] → 4
#
# APPROACH: Two-pass greedy.
# Pass 1 (left to right): if ratings[i] > ratings[i-1], candy[i] = candy[i-1] + 1
# Pass 2 (right to left): if ratings[i] > ratings[i+1], candy[i] = max(candy[i], candy[i+1]+1)

# @lc code=start
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = [1] * n

        # Left-to-right pass
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1

        # Right-to-left pass
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)

        return sum(candy)
        # Time: O(n)  Space: O(n)
# @lc code=end
