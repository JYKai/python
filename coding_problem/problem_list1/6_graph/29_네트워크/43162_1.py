def DFS(computers, visited, node):
    visited[node] = True
    for idx, connected in enumerate(computers[node]):
        if not visited[idx] and connected:
            DFS(computers, visited, idx)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            DFS(computers, visited, i)
            answer += 1
    return answer
