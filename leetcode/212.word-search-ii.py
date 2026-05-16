#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#

# @lc code=start
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if '#' in node:
                result.append(node['#'])
                del node['#']
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            tmp = board[r][c]
            if tmp not in node:
                return
            board[r][c] = '#'
            next_node = node[tmp]
            dfs(r+1, c, next_node)
            dfs(r-1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)
            board[r][c] = tmp

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result
# @lc code=end
