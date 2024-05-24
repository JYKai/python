from collections import deque

def solution(maps):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    n, m = len(maps), len(maps[0])
    visited = [[[False, False] for _ in range(m)] for _ in range(n)] # [lever off, lever on]

    def BFS(x, y):     
        q = deque([(x, y, False, 0)]) # (x, y, lever, count)
        visited[x][y][0] = True
        
        while q:
            cx, cy, cl, cc = q.popleft()
            
            if maps[cx][cy] == 'E' and cl:
                return cc
            
            if maps[cx][cy] == 'L':
                cl = True
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                    next_cl_state = 1 if cl else 0
                    if not visited[nx][ny][next_cl_state]:
                        visited[nx][ny][next_cl_state] = True
                        q.append((nx, ny, cl, cc + 1))
        
        return -1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                return BFS(i, j)
