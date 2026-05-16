#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#
# PROBLEM:
# There are n courses labeled 0 to n-1. Prerequisites: [a,b] means must take b before a.
# Return the ordering of courses to finish all of them, or [] if impossible.
# Example: n=4, [[1,0],[2,0],[3,1],[3,2]] → [0,2,1,3] or [0,1,2,3]
#
# APPROACH: Topological Sort using Kahn's algorithm (BFS with in-degree).
# Repeatedly pick nodes with in-degree 0, add to result, reduce neighbors' in-degrees.

# @lc code=start
from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        # Start with all courses that have no prerequisites
        queue = deque(c for c in range(numCourses) if in_degree[c] == 0)
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:    # all prerequisites satisfied
                    queue.append(neighbor)

        return order if len(order) == numCourses else []   # [] if cycle detected
        # Time: O(V + E)  Space: O(V + E)
# @lc code=end
