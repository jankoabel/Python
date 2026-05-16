#
# @lc app=leetcode id=1125 lang=python
#
# [1125] Smallest Sufficient Team (HARD)
#
# PROBLEM:
# Given required skills and a list of people (each with some skills),
# find the smallest team that covers all required skills.
# Example: req_skills=["java","nodejs","reactjs"],
#          people=[["java"],["nodejs"],["nodejs","reactjs"]] → [0,2]
#
# APPROACH: Bitmask DP.
# Represent each person's skills as a bitmask.
# dp[mask] = minimum team to cover skills in mask.

# @lc code=start
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        skill_idx = {s: i for i, s in enumerate(req_skills)}
        n = len(req_skills)
        full = (1 << n) - 1

        # dp[mask] = list of person indices forming the team
        dp = [None] * (1 << n)
        dp[0] = []

        for i, person in enumerate(people):
            skill_mask = 0
            for s in person:
                if s in skill_idx:
                    skill_mask |= (1 << skill_idx[s])

            for mask in range(full, -1, -1):
                if dp[mask] is None:
                    continue
                new_mask = mask | skill_mask
                if dp[new_mask] is None or len(dp[new_mask]) > len(dp[mask]) + 1:
                    dp[new_mask] = dp[mask] + [i]

        return dp[full]
        # Time: O(people * 2^skills)  Space: O(2^skills)
# @lc code=end
