# 그래프 개념(Graph)
그래프는 노드(vertex)와 간선(edge)을 이용한 비선형 데이터구조이며, 주로 데이터 간의 관계를 표현하는데 사용한다.

</br>

## 그래프의 특징과 종류
### 흐름을 표현하는 방향성
- 방향 그래프: 방향이 있는 간선을 포함하는 그래프
- 무뱡향 그래프: 방향이 없는 간선을 포함하는 그래프

### 흐름의 정도를 표현하는 가중치
- 가중치 그래프: 정도를 표현한 가중치가 있는 그래프

### 시작과 끝이 연결 여부를 보는 순환
- 순환 그래프: 순환이 존재하는 그래프
- 비순환 그래프: 순환이 존재하지 않는 그래프

</br>

## 그래프 구현
그래프의 노드, 간선, 방향, 가중치를 사용

### 인접 행렬(adjacency matrix)그래프 표현
배열을 활용한 인접 행렬을 활용하여 구현한다.
- 배열의 인덱스는 노드, 배열의 값은 노드의 가중치로 생각하여 표현  

**장점**  
- 간선의 정보를 확인할 때 시간 복잡도 = O(1)
- 구현 난이도가 낮음

**단점**  
- 인접 행렬로 희소 그래프를 표현하는 경우, 최악의 경우를 고려해서 크기를 결정해야 한다.
- 노드들의 값의 차이가 매우 큰 그래프를 표현하는 경우, 인접 행렬의 크기가 커질 수 있다.

### 인접 리스트(adjacency list) 그래프 표현
**인접 리스트 그래프 표현 방식**  
1. 노드 개수만큼 배열을 준비한다.
2. 배열의 인덱스는 각 시작 노드를 의미하며 배열의 값에는 다음 노드를 연결한다.

**장점**  
- 실제 연결된 노드에 대해서만 노드의 값을 노드에 담아 연결하기만 하면 되므로 메모리를 아낄 수 있다.

**단점**  
- 연결된 노드 개수가 많으면 노드를 연결한 리스트의 길이만큼 탐색해야 하므로 시간 복잡도 = O(N)

***따라서, 노드 개수가 1,000개 미만으로 주어지는 경우에는 인접 행렬을 사용하면 좋다.***

</br>

# 그래프 탐색
## 깊이 우선 탐색(depth-first search, DFS)
시작 노드부터 탐색을 시작하여 간선을 따라 최대 깊이 노드까지 이동하며 차례대로 방문한다. 최대 깊이 노드까지 방문한 뒤 이전에 방문한 노드를 거슬러 올라가며 해당 노드와 연결된 노드 중 방문하지 않은 노드로 다시 최대 깊이까지 차례대로 방문하는 탐색 알고리즘
- 탐색 후 되돌아오는 특성이 있다.
    - 모든 가능한 해를 찾는 백트래킹 알고리즘을 구현할 때나 그래프의 사이클을 감지해야 하는 경우 활용할 수 있다.
    - 코딩 테스트에서는 탐색을 해야할 때, 최단 경로를 찾는 문제가 아니라면 DFS를 우선 고려해보는 것이 좋다.

</br>

## 너비 우선 탐색(breadth first search, BFS)
시작 노드와 거리가 가장 가까운 노드를 우선하여 방문하는 방식의 탐색 알고리즘
- 시작 노드로부터 직접 간선으로 연결된 모든 노드를 먼저 방문하기 때문에 가중치가 없는 그래프에서 최단 경로를 보장한다.
    - 미로 찾기 문제에서 최단 경로를 찾거나, 네트워크 분석 문제를 풀 때 활용할 수 있다.

</br>

## 연습문제
1. 깊이 우선 탐색 순회  
깊이 우선 탐색으로 모든 그래프의 노드를 순회하는 함수 solution()을 작성하시오.

**입출력의 예**  
| graph | start | return |
| ---- | :--- | ----- | 
| [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']] | 'A' | ['A', 'B', 'C', 'D', 'E'] |

```python
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
```

2. 너비 우선 탐색 순회  
너비 우선 탐색으로 모든 노드를 순회하는 함수 solution()을 작성하시오.

**입출력의 예**  
| graph | start | return |
| ---- | :--- | ----- | 
| [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)] | 1 | [1, 2, 3, 4, 5, 0] |

```python
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
```

</br>

# 그래프 최단 경로 구하기
그래프 종류에 따라 다르게 해석될 수 있는 주제
- 가중치가 없는 그래프: 간선 개수가 가장 적은 경로가 최단 경로
- 가중치가 있는 그래프: 시작 노드에서 끝 노드까지 이동할 때 거치는 간선의 가중치의 총합이 최소가 되는 경로

## 다익스트라 알고리즘
가중치가 있는 그래프의 최단 경로를 구하는 문제는 대부분 다익스트라 알고리즘을 사용한다고 볼 수 있는 알고리즘  

**동작 과정**  
1. 시작 노드를 설정하고 시작 노드로부터 특정 노드까지의 최소 비용을 저장할 공간과 직전 노드를 저장할 공간을 마련한다.
    - 최소 비용을 저장할 공간은 모두 매우 큰 값(INF)으로 초기화한다. 
    - 시작 노드의 최소 비용은 0, 직전 노드는 자신으로 한다.

2. 해당 노드를 통해 방문할 수 있는 노드 중, 즉 아직 방문하지 않은 노드 중 현재까지 구한 최소 비용이 가장 적은 노드를 선택한다.
    - 해당 노드를 거쳐서 각 노드까지 가는 최소 비용과 현재까지 구한 최소 비용을 비교해서 작은 값을 각 노드의 최소 비용으로 갱신한다.
    - 이때 직전 노드도 같이 갱신한다.

3. 노드 개수에서 1을 뺀 만큼 반복한다.

> Q. 음의 가중치가 있는 그래프에서 다익스트라 알고리즘은 어떨까?  
다익스트라 알고리즘은 양의 가중치만 있는 그래프에서만 동작하므로 음의 가중치가 있는 그래프에서 제대로 동작하지 않는다.

</br>

## 벨만-포드 알고리즘
매 단계마다 모든 간선의 가중치를 다시 확인하여 최소 비용을 갱신하므로 음의 가중치를 가지는 그래프에서도 최단 경로를 구할 수 있다.

**동작 과정**  
1. 시작 노드를 설정한 다음 시작 노드의 최소 비용은 0, 나머지 노드는 INF로 초기화 한다. 이후, 최소 비용을 갱신할 때 직전 노드도 갱신한다.

2. 노드 개수 -1만큼 다음 연산을 반복한다.
    - 시작 노드에서 갈 수 있는 각 노드에 대하여 전체 노드 각각을 거쳐갈 때 현재까지 구한 최소 비용보다 더 적은 최소 비용이 있는지 확인하여 갱신한다. 최소 비용을 갱신할 때, V의 직전 노드 값도 같이 갱신한다.

3. 과정 2를 마지막으로 한 번 더 수행하여 갱신되는 최소 비용이 있는지 확인한다. 만약 있다면 음의 순환이 있음을 의미한다.

### 왜 정점 개수 -1만큼 반복하는가? 
매 연산마다 최단 경로가 1개씩 확정되므로!

## 왜 한 번 더 연산을 반복하는가?
음의 순환을 찾기 위해!

</br>

## 연습문제
1. 다익스트라 알고리즘  
주어진 그래프와 시작 노드를 이용하여 다익스트라 알고리즘을 구현하는 solution() 함수를 작성하시오. 반환값은 시작 노드부터, 각 노드까지 최소 비용과 최단 경로를 포함하는 리스트이다.

**입출력의 예**  
| graph | start | return |
| ---- | :--- | ----- | 
| {'A': {'B': 9, 'C': 3}, 'B': {'A': 5}, 'C': {'B': 1}} | 'A' | {'A': 0, 'B': 4, 'C': 3, {'A': ['A'], 'B': ['A', 'C', 'B'], 'C': ['A', 'C']}} |

```python
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
```

2. 벨만-포드 알고리즘  
벨만-포드 알고리즘을 구현한 solution() 함수를 구현하시오.  
노드 정보의 구성은 (노드, 가중치)와 같다. 반환값은 최단 거리를 담은 distance와 최단 거리와 함께 관리할 직전 노드 predecessor를 리스트에 차례대로 담아서 반환하면 된다. predecessor에서 시작 노드는 None으로 하고, 음의 가중치 순회가 있다면 [-1]을 반환하시오.

**입출력의 예**  
| graph | start | return |
| ---- | :--- | ----- | 
| [[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]] | 0 | [-1] |

```python
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
```

</br>

# 실전문제

<details>
<summary>28. 게임 맵 최단거리</summary>
<div markdown='1'>

---


---
</div>
</details>


<details>
<summary>29. 네트워크</summary>
<div markdown='1'>

---


---
</div>
</details>


<details>
<summary>30. 배달</summary>
<div markdown='1'>

---


---
</div>
</details>


<details>
<summary>31. 경주로 건설</summary>
<div markdown='1'>

---


---
</div>
</details>


<details>
<summary>32. 전력망을 둘로 나누기</summary>
<div markdown='1'>

---


---
</div>
</details>