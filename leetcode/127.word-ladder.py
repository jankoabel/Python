#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder (HARD)
#
# PROBLEM:
# Given beginWord, endWord, and a wordList, return the length of the shortest
# transformation sequence from beginWord to endWord, where each step changes
# exactly one letter and the new word must be in wordList.
# Return 0 if no such sequence exists.
# Example: beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log","cog"] → 5
#
# APPROACH: BFS (shortest path). Use wildcard patterns to group words
# (e.g., "h*t" maps to ["hit","hot"]). BFS from beginWord to endWord.

# @lc code=start
from collections import defaultdict, deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Build pattern → words map
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

        return 0
        # Time: O(n * L^2)  Space: O(n * L^2)
# @lc code=end
