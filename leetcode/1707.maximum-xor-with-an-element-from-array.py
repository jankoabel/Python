#
# @lc app=leetcode id=1707 lang=python
#
# [1707] Maximum XOR With an Element From Array (HARD)
#
# PROBLEM:
# Given nums and queries[i]=[xi, mi], for each query return max XOR of xi with
# any element of nums that is <= mi. Return -1 if no such element.
#
# APPROACH: Offline processing. Sort queries by mi. Sort nums.
# Build a Trie incrementally (only nums <= mi). For each query, find max XOR.

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums.sort()
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][1])

        root = TrieNode()

        def insert(num):
            node = root
            for bit in range(31, -1, -1):
                b = (num >> bit) & 1
                if not node.children[b]:
                    node.children[b] = TrieNode()
                node = node.children[b]

        def query_max_xor(num):
            node = root
            xor = 0
            for bit in range(31, -1, -1):
                b = (num >> bit) & 1
                want = 1 - b  # prefer opposite bit for max XOR
                if node.children[want]:
                    xor |= (1 << bit)
                    node = node.children[want]
                elif node.children[b]:
                    node = node.children[b]
                else:
                    return -1
            return xor

        result = [-1] * len(queries)
        num_idx = 0

        for q_idx, (xi, mi) in sorted_queries:
            while num_idx < len(nums) and nums[num_idx] <= mi:
                insert(nums[num_idx])
                num_idx += 1
            if num_idx > 0:
                result[q_idx] = query_max_xor(xi)

        return result
        # Time: O((n + q) log(max_val))  Space: O(n * 32)
# @lc code=end
