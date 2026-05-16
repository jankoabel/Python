#
# @lc app=leetcode id=1203 lang=python
#
# [1203] Sort Items by Groups Respecting Dependencies (HARD)
#
# PROBLEM:
# Items belong to groups. Sort items such that:
# - Items in same group are consecutive
# - beforeItems[i] come before i
# Return any valid order or [] if impossible.
#
# APPROACH: Two-level topological sort.
# 1. Sort within groups (items within a group).
# 2. Sort groups between groups.
# Build both intra-group and inter-group dependency graphs. Topo sort both.

# @lc code=start
from collections import defaultdict, deque

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        # Assign unique group id to ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Build item graph and group graph
        item_graph   = defaultdict(list)
        item_indeg   = [0] * n
        group_graph  = defaultdict(set)
        group_indeg  = [0] * m

        for i in range(n):
            for pre in beforeItems[i]:
                item_graph[pre].append(i)
                item_indeg[i] += 1
                if group[pre] != group[i]:
                    if i not in group_graph[group[pre]]:
                        group_graph[group[pre]].add(i)
                        group_indeg[group[i]] += 1

        def topo_sort(graph, indeg, nodes):
            queue = deque([node for node in nodes if indeg[node] == 0])
            result = []
            while queue:
                node = queue.popleft()
                result.append(node)
                for nb in graph[node]:
                    indeg[nb] -= 1
                    if indeg[nb] == 0:
                        queue.append(nb)
            return result if len(result) == len(nodes) else []

        # Topo sort items
        item_order = topo_sort(item_graph, item_indeg, range(n))
        if not item_order:
            return []

        # Topo sort groups
        group_order = topo_sort(group_graph, group_indeg, range(m))
        if not group_order:
            return []

        # Group items by their group
        group_items = defaultdict(list)
        for item in item_order:
            group_items[group[item]].append(item)

        return [item for g in group_order for item in group_items[g]]
        # Time: O(n + m + E)  Space: O(n + m + E)
# @lc code=end
