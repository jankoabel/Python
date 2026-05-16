#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Greedy insight: the most frequent task determines the minimum time
        # Arrange tasks in chunks of (n+1): [A, B, C, idle, A, B, C, idle, ...]
        # Formula: (max_count - 1) * (n + 1) + number_of_tasks_with_max_count
        # But if we have enough variety, we might not need idle time at all
        counts = Counter(tasks)
        max_count = max(counts.values())
        # How many tasks have the maximum frequency?
        tasks_with_max = sum(1 for c in counts.values() if c == max_count)

        # Minimum slots = (n+1) slots per "frame" * (max_count-1) frames + last partial frame
        min_slots = (max_count - 1) * (n + 1) + tasks_with_max

        # If we have enough tasks to fill all slots, no idle time needed
        return max(min_slots, len(tasks))
        # Time: O(n)  Space: O(1) — at most 26 task types
# @lc code=end
