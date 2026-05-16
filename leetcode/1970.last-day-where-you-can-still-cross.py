#
# @lc app=leetcode id=1970 lang=python
#
# [1970] Last Day Where You Can Still Cross (HARD)
#
# PROBLEM:
# An m×n grid starts all land. Cells flood on given days.
# Find the last day you can still walk from top row to bottom row (on land cells).
# Example: row=2, col=2, cells=[[1,1],[2,1],[1,2],[2,2]] → 2
#
# APPROACH: Binary search on day + BFS to check if path exists.
# Or: Reverse Union-Find — process cells from last to first.
# Connect land cells. Use virtual nodes for top and bottom rows.

# @lc code=start
class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        def bfs(day):
            grid = [[1] * col for _ in range(row)]  # 1 = land
            for r, c in cells[:day]:
                grid[r-1][c-1] = 0
            from collections import deque
            queue = deque()
            for c in range(col):
                if grid[0][c]:
                    queue.append((0, c))
                    grid[0][c] = 0
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))
            return False

        lo, hi = 1, len(cells)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if bfs(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
        # Time: O(m*n * log(m*n))  Space: O(m*n)
# @lc code=end
