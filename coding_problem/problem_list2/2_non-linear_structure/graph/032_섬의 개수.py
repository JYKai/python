# 내 풀이
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def BFS(r, c):
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
            while q:
                cr, cc = q.popleft()
                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))

        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]

        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and not visited[r][c]:
                    cnt += 1
                    BFS(r, c)

        return cnt