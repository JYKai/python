from collections import defaultdict

def solution(graph, start):
    # 1. 그래프를 인접 리스트로 변환
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
    
    # 2. DFS 탐색 함수
    def dfs(node, visited, result):
        visited.add(node) # 3. 현재 노드를 방문한 노드들의 집합에 추가
        result.append(node) # 4. 현재 노드를 결과 리스트에 추가
        for neighbor in adj_list.get(node, []): # 5. 현재 노드와 인접한 노드 순회
            if neighbor not in visited:
                dfs(neighbor, visited, result)

    # DFS 순회한 결과를 반환
    visited = set()
    result = []

    dfs(start, visited, result)

    return result

graph = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
start = 'A'

print(solution(graph, start))