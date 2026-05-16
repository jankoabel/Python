#
# @lc app=leetcode id=2050 lang=python
#
# [2050] Parallel Courses III (HARD)
#
# PROBLEM:
# n courses with time[i] to complete. Course j can start after all prerequisites done.
# Return minimum number of months to complete all courses.
# Example: n=3, relations=[[1,3],[2,3]], time=[3,2,5] → 8 (1→3: 3+5=8)
#
# APPROACH: Topological sort (Kahn's). dp[node] = earliest finish time.
# dp[node] = time[node] + max(dp[prereq] for all prereq).

# @lc code=start
from collections import defaultdict, deque

class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        indeg = [0] * (n + 1)

        for pre, nxt in relations:
            graph[pre].append(nxt)
            indeg[nxt] += 1

        dp = time[:]   # dp[i-1] = earliest finish of course i (0-indexed here)
        dp = [0] + time  # 1-indexed

        queue = deque([i for i in range(1, n+1) if indeg[i] == 0])

        while queue:
            node = queue.popleft()
            for nb in graph[node]:
                dp[nb] = max(dp[nb], dp[node] + time[nb - 1])
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    queue.append(nb)

        return max(dp[1:])
        # Time: O(V + E)  Space: O(V + E)
# @lc code=end
