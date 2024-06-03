from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque()
    q.append([0, 0, 1])
    
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        cx, cy, cc = q.popleft()
        
        if [cy, cx] == [n - 1, m - 1]:
            return cc
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and visited[ny][nx] != 1:
                visited[ny][nx] = 1
                q.append([nx, ny, cc + 1])
                
    return answer
