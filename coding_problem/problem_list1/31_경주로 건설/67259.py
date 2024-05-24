import heapq

def solution(board):
    answer = float('inf')
    n = len(board)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = []
    heapq.heappush(q, (0, 0, 0, -1))
    
    visited = [[[float('inf') for _ in range(4)] for _ in range(n)] for _ in range(n)]
    visited[0][0][0] = visited[0][0][1] = visited[0][0][2] = visited[0][0][3] = 0
    
    while q:
        cost, cx, cy, direction = heapq.heappop(q)
        
        if [cx, cy] == [n - 1, n - 1]:
            answer = min(answer, cost)
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[ny][nx] != 1:
                new_cost = cost + 100 if direction == i or direction == -1 else cost + 600
                
                if visited[ny][nx][i] >= new_cost:
                    visited[ny][nx][i] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny, i))
                    
    return answer
