#
# @lc app=leetcode id=630 lang=python
#
# [630] Course Schedule III (HARD)
#
# PROBLEM:
# There are n courses [duration, deadline]. You can take one course at a time.
# Return the maximum number of courses you can take.
# Example: courses=[[100,200],[200,1300],[1000,1250],[2000,3200]] → 3
#
# APPROACH: Greedy + Max-heap.
# Sort by deadline. For each course, try to add it.
# If adding it exceeds its deadline, replace the longest course taken so far
# (if it's longer than current course — this frees time without losing a course).

# @lc code=leetcode
import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[1])  # sort by deadline
        heap = []  # max-heap of durations (negate)
        time = 0

        for duration, deadline in courses:
            heapq.heappush(heap, -duration)
            time += duration
            if time > deadline:
                # Remove the longest course to free the most time
                time += heapq.heappop(heap)  # adds back negative (subtracts)

        return len(heap)
        # Time: O(n log n)  Space: O(n)
# @lc code=end
