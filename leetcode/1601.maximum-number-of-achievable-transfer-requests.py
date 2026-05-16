#
# @lc app=leetcode id=1601 lang=python
#
# [1601] Maximum Number of Achievable Transfer Requests (HARD)
#
# PROBLEM:
# There are n buildings. Each request moves one person from building from_i to to_i.
# A set of requests is achievable if each building has same in/out count (balanced).
# Return max achievable requests.
# Example: n=5, requests=[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]] → 5
#
# APPROACH: Bitmask brute force (m <= 16).
# For each subset of requests, check if the net flow to/from each building is 0.

# @lc code=start
class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        m = len(requests)
        best = 0

        for mask in range(1 << m):
            net = [0] * n
            count = bin(mask).count('1')
            if count <= best:
                continue  # can't improve
            for i in range(m):
                if mask & (1 << i):
                    net[requests[i][0]] -= 1
                    net[requests[i][1]] += 1
            if all(x == 0 for x in net):
                best = count

        return best
        # Time: O(2^m * (m + n))  Space: O(n)
# @lc code=end
