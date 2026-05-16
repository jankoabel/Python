#
# @lc app=leetcode id=211 lang=python
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class WordDictionary(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            if c not in node.children:
                return False
            return dfs(node.children[c], i + 1)
        return dfs(self, 0)
# @lc code=end
