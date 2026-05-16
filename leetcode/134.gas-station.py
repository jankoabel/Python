#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Key insight: if total gas >= total cost, a solution always exists
        # Greedy: whenever our running tank goes negative, the start must be AFTER current i
        # Proof: any station before i also couldn't have gotten past i (they'd face the same deficit)

        if sum(gas) < sum(cost):
            return -1   # impossible — not enough fuel overall

        tank = 0
        start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:         # can't reach station i+1 from current start
                start = i + 1   # try starting from the next station
                tank = 0        # reset tank

        return start
        # Time: O(n)  Space: O(1)
# @lc code=end
