from collections import deque, defaultdict

def solution(graph, start):

    # 그래프를 인접 리스트로 변환
    adj_list = defaultdict(list)
    for u, v in graph:
        adj_list[u].append(v)
    
    q = deque()
    q.append(start)

    result = []
    visited = set()
    while q:
        current_num = q.popleft()
        visited.add(current_num)
        result.append(current_num)

        for next_num in adj_list.get(current_num, []):
            if next_num not in visited:
                q.append(next_num)

    return result

graph = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
start = 1

print(solution(graph, start))