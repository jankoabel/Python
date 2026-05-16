#
# @lc app=leetcode id=1376 lang=python
#
# [1376] Time Needed to Inform All Employees
#
# PROBLEM:
# Company has n employees. headID is the CEO. manager[i] = manager of employee i.
# informTime[i] = time needed to inform all direct subordinates.
# Return total time needed to inform all employees.
# Example: n=6, headID=2, manager=[-1,2,0,0,2,2], informTime=[0,0,0,0,0,0,2,4,0,0,0,7,0] → ?
#
# APPROACH: Build adjacency list (manager → subordinates).
# DFS from headID: time to inform subtree = informTime[node] + max(dfs(sub) for all subs).

# @lc code=start
from collections import defaultdict

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        subordinates = defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                subordinates[mgr].append(emp)

        def dfs(emp):
            if not subordinates[emp]:
                return 0
            return informTime[emp] + max(dfs(sub) for sub in subordinates[emp])

        return dfs(headID)
        # Time: O(n)  Space: O(n)
# @lc code=end
