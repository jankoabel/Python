#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
# @lc code=end
