#
# @lc app=leetcode id=841 lang=python
#
# [841] Keys and Rooms
#
# PROBLEM:
# There are n rooms (0..n-1). Room 0 is unlocked. Each room has a list of keys
# to other rooms. Return true if you can visit all rooms.
# Example: rooms=[[1],[2],[3],[]] → True  ;  rooms=[[1,3],[3,0,1],[2],[0]] → False
#
# APPROACH: DFS/BFS from room 0. Track visited rooms.
# If visited count == n at end, all rooms can be entered.

# @lc code=start
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set([0])
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == len(rooms)
        # Time: O(V + E)  Space: O(V)
# @lc code=end
