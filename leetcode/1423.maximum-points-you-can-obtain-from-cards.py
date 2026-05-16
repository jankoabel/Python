#
# @lc app=leetcode id=1423 lang=python
#
# [1423] Maximum Points You Can Obtain from Cards
#
# PROBLEM:
# There are n cards in a row with values cardPoints[]. In each step you can
# take from the leftmost or rightmost card. Take exactly k cards.
# Return maximum score possible.
# Example: cardPoints=[1,2,3,4,5,6,1], k=3 → 12 (take 1,6,5 from right)
#
# APPROACH: Instead of tracking which k cards to take, find the minimum-sum
# subarray of length n-k (the cards left behind).
# Answer = total_sum - min_window_sum.

# @lc code=start
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        window_size = n - k
        total = sum(cardPoints)

        if window_size == 0:
            return total

        # Find minimum window of size window_size
        window_sum = sum(cardPoints[:window_size])
        min_window = window_sum

        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, window_sum)

        return total - min_window
        # Time: O(n)  Space: O(1)
# @lc code=end
