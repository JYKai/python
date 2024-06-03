import heapq

def solution(graph, start):
    # 1. 모든 노드의 거리 값을 무한대로 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 # 2. 시작 노드의 거리 값은 0으로 초기화

    queue = []
    heapq.heappush(queue, [distances[start], start]) # 3. 시작 노드를 큐에 삽입
    paths = {start: [start]} # 4. 시작 노드의 경로를 초기화

    while queue:
        # 5. 현재 가장 거리 값이 작은 노드를 가져옴
        current_distance, current_node  = heapq.heappop(queue)
        # 6. 만약 현재 노드의 거리 값이 큐에서 가져온 거리 값보다 크면, 해당 노드는 이미 처리한 것으로 무시
        if distances[current_node] < current_distance:
            continue
        
        # 7. 현재 노드와 인접한 노드들의 거리 값을 계산하여 업데이트
        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight
            # 8. 현재 계산한 거리 값이 기존 거리 값보다 작으면 최소 비용 및 최단 경로 업데이트
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance # 최소 비용 업데이트
                paths[adjacent_node] = paths[current_node] + [adjacent_node] # 최댄 경로 업데이트

                # 9. 최소 경로가 갱신된 노드를 비용과 함께 큐에 푸시
                heapq.heappush(queue, [distance, adjacent_node])
        
    # 10. paths 딕셔너리를 노드 번호에 따라 오름차순 정렬하여 반환
    sorted_paths = {node: paths[node] for node in sorted(paths)}

    return [distances, sorted_paths]

graph = {'A': {'B': 9, 'C': 3}, 
         'B': {'A': 5}, 
         'C': {'B': 1}}

start = 'A'

print(solution(graph, start))