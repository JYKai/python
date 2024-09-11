def solution(graph, source):
    # 1. 그래프의 노드 수
    num_vertices = len(graph)

    # 2. 거리 배열 초기화
    distance = [float('inf')] * num_vertices
    distance[source] = 0

    # 3. 직전 경로 배열 초기화
    predecessor = [None] * num_vertices

    # 4. 간선 수 만큼 반복하여 최단 경로 갱신
    for temp in range(num_vertices - 1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                # 5. 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
                if distance[u] + weight < distance[v]:
                    # 6. 최단 거리 갱신
                    distance[v] = distance[u] + weight
                    # 7. 직전 경로 업데이트
                    predecessor[v] = u

    # 8. 음의 가중치 순회 체크
    for u in range(num_vertices):
        for v, weight in graph[u]:
            # 9. 현재 노드 u를 거쳐서 노드 v로 가는 경로의 거리가 기존에 저장된 노드 v까지의 거리보다 짧은 경우
            if distance[u] + weight < distance[v]:
                # 10. 음의 가중치 순회가 발견되었으므로 [-1]을 반환한다.
                return [-1]

    return [distance, predecessor]

graph = [[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]]
source = 0

print(solution(graph, source))