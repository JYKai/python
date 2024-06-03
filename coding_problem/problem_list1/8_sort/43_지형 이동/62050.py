from heapq import heappush, heappop

def solution(land, height):
    answer = 0
    
    n = len(land)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = []
    heappush(q, [0, 0, 0])
    visited = [[False] * n for _ in range(n)]
    
    while q:
        cost, x, y = heappop(q)
        if not visited[y][x]:
            visited[y][x] = True
            answer += cost
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    temp = abs(land[y][x] - land[ny][nx])
                    if temp > height:
                        new_cost = temp
                    else:
                        new_cost = 0
                    heappush(q, [new_cost, nx, ny])
                    
    return answer
