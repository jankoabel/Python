#
# @lc app=leetcode id=2092 lang=python
#
# [2092] Find All People With Secret (HARD)
#
# PROBLEM:
# n people. Person 0 has a secret. meetings[i]=[x,y,time].
# At each meeting, if either knows the secret, both learn it.
# Return all people who eventually know the secret.
# Example: n=6, meetings=[[1,2,5],[2,3,8],[1,5,10]], firstPerson=1 → [0,1,2,3,5]
#
# APPROACH: Group meetings by time. Process each time group:
# 1. Union-Find: merge participants in each meeting.
# 2. After processing each time, un-merge anyone who doesn't connect to secret-knower.

# @lc code=start
from collections import defaultdict

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        union(0, firstPerson)

        # Group meetings by time
        time_meetings = defaultdict(list)
        for x, y, t in meetings:
            time_meetings[t].append((x, y))

        for t in sorted(time_meetings):
            participants = set()
            for x, y in time_meetings[t]:
                union(x, y)
                participants.add(x)
                participants.add(y)
            # Reset anyone who isn't connected to person 0 after this round
            for p in participants:
                if find(p) != find(0):
                    parent[p] = p

        return [i for i in range(n) if find(i) == find(0)]
        # Time: O(m log m * alpha(n))  Space: O(n + m)
# @lc code=end
