from collections import deque

def solution(n, computers):
    answer = 0
    
    def BFS(computer, visited):
        q = deque([computer])
        visited[computer] = True
        while q:
            comp = q.popleft()
            for idx, connected in enumerate(computers[comp]):
                if connected and not visited[idx]:
                    visited[idx] = True
                    q.append(idx)
    
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            BFS(i, visited)
            answer += 1
            
    return answer