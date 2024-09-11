import heapq

def solution(board):
    answer = float('inf')
    
    n = len(board)
    m = len(board[0])
    hq = []

    heapq.heappush(hq, [0, 0, 0, -1])
    
    visited = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]
    
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    while hq:
        cost, cr, cc, cd = heapq.heappop(hq)

        if cr == (n - 1) and cc == (m - 1):
            answer = min(answer, cost)
            
        for next_direction in range(4):
            nr, nc = cr + dr[next_direction], cc + dc[next_direction]
            if 0 <= nr < n and 0 <= nc < m and not board[nr][nc]:
                new_cost = cost + 100 if cd == -1 or cd == next_direction else cost + 600
                
                if visited[nr][nc][next_direction] > new_cost:
                    visited[nr][nc][next_direction] = new_cost
                    heapq.heappush(hq, [new_cost, nr, nc, next_direction])
                    
    return answer