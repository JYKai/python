def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    visited = [False] * n
    
    def DFS(k, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                DFS(k - dungeons[i][1], cnt + 1)
                visited[i] = False
            
    DFS(k, 0)
    return answer
