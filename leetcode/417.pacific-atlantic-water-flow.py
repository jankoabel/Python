#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        def bfs(starts):
            visited = set(starts)
            queue = list(starts)
            while queue:
                r, c = queue.pop()
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited
        pacific = bfs([(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)])
        atlantic = bfs([(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)])
        return [[r, c] for r, c in pacific & atlantic]
# @lc code=end
