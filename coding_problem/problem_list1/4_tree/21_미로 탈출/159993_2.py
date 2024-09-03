import heap

def find_start_location(maps, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 'S':
                return [r, c]

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # 시작 위치찾기
    start_r, start_c = find_start_location(maps, rows, cols)
    
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    
    heap = []
    heapq.heappush(heap, [0, start_r, start_c, False])
    visited = [[[False, False] for _ in range(cols)] for _ in range(rows)]
    
    while heap:
        cost, cr, cc, is_lever = heapq.heappop(heap)
        
        if visited[cr][cc][is_lever]:
            continue
            
        visited[cr][cc][is_lever] = True
        
        if maps[cr][cc] == 'L':
            is_lever = True
            
        if maps[cr][cc] == 'E' and is_lever:
            return cost
        
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] != 'X':
                heapq.heappush(heap, [cost + 1, nr, nc, is_lever])
                    
    return -1
