import heapq

def is_blocked(maps, row, col):
    return True if (maps[row - 2][col - 1] == 0 and maps[row - 1][col - 2] == 0) else False

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    if is_blocked(maps, n, m):
        return -1
    
    hq = []
    heapq.heappush(hq, [1, 0, 0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    
    while hq:
        cost, cr, cc = heapq.heappop(hq)

        if [cr, cc] == [n - 1, m - 1]:
            return cost
        
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc]:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(hq, [cost + 1, nr, nc])
    
    return -1