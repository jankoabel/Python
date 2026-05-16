#
# @lc app=leetcode id=269 lang=python
#
# [269] Alien Dictionary (HARD)
#
# PROBLEM:
# Given a list of words sorted lexicographically by the rules of an alien language,
# derive the order of characters in the alien alphabet. Return any valid order,
# or "" if invalid (cycle).
# Example: words=["wrt","wrf","er","ett","rftt"] → "wertf"
#
# APPROACH: Build a directed graph from adjacent words (find first differing char).
# Topological sort (Kahn's BFS). Detect cycle if not all nodes processed.

# @lc code=start
from collections import defaultdict, deque

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Initialize in-degree for all unique chars
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            # Check invalid: longer word is prefix of shorter
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # Kahn's BFS
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return ''.join(result) if len(result) == len(in_degree) else ""
        # Time: O(C) where C=total chars  Space: O(1) — fixed 26 chars
# @lc code=end
