#
# @lc app=leetcode id=2076 lang=python
#
# [2076] Process Restricted Friend Requests (HARD)
#
# PROBLEM:
# n people with restrictions[i]=[x,y] (x and y cannot be in the same friend group).
# Process requests[j]=[u,v] — can u and v become friends without violating restrictions?
# Return boolean array.
#
# APPROACH: Union-Find with rollback (or check before merging).
# For each request: temporarily merge u and v, check all restrictions.
# If any restriction is violated (both in same component), reject.

# @lc code=start
class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry: return
            if rank[rx] < rank[ry]: rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]: rank[rx] += 1

        result = []

        for u, v in requests:
            ru, rv = find(u), find(v)
            # Check if merging violates any restriction
            ok = True
            for x, y in restrictions:
                rx, ry = find(x), find(y)
                if (rx == ru and ry == rv) or (rx == rv and ry == ru):
                    ok = False
                    break
            if ok:
                union(u, v)
            result.append(ok)

        return result
        # Time: O(q * r * alpha(n))  Space: O(n)
# @lc code=end
