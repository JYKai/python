# 비선형 자료구조
데이터 요소가 순차적으로 또는 선형으로 배열되지 않은 자료구조
- 선형에 비해 구현하기 다소 어렵지만, 메모리를 좀 더 효율적으로 활용할 수 있다는 장점이 있다.

## 그래프(Graph)
그래프 이론에서 그래프란 객체의 일부 쌍(pair)들이 '연관되어'있는 객체 집합 구조를 말한다.

### 그래프 순회
그래프 탐색이라고도 불리우며 그래프의 각 정점을 방문하는 과정을 말한다.

**깊이 우선 탐색(Depth-First Search, DFS)**
- 주로 스택으로 구현하거나 재귀로 구현
- 백트래킹에 사용된다.

재귀 구조로 구현
```python
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph(v):
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
```

스택을 이용한 구현
```python
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
```

**너비 우선 탐색(Breadth-First Search, BFS)**
- 큐로 구현하며 최단 경로를 구하는 문제에 주로 사용된다.

큐를 이용한 반복 구조로 구현
```python
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
```

### 백트래킹(Backtracking)
해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기해 정답을 찾아가는 범용적인 알고리즘

**제약 충족 문제(Constraint Satisfaction Problems, CSP)**  
수많은 제약 조건을 충족하는 상태를 찾아내는 수학 문제

<details>
<summary>032. 섬의 개수</summary>
<div markdown='1'>

---
1. DFS로 그래프 탐색
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            grid[i][j] = 0
            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count
```
- 중첩 함수를 사용하여 DFS 구현

---
</div>
</details>


<details>
<summary>033. 전화 번호 문자 조합</summary>
<div markdown='1'>

---
1. 모든 조합 탐색
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        
        # 예외 처리
        if not digits:
            return []
        
        dic = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}
        
        result = []
        dfs(0, "")
        
        return result
```

---
</div>
</details>