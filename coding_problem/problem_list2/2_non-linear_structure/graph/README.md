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


## Problems
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


<details>
<summary>034. 순열</summary>
<div markdown='1'>

---
1. DFS를 활용한 순열 생성
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
            
            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        return results
```
- ```prev_elements[:]``` : 값을 복사하는 형태로 참조 관계를 갖지 않도록 처리한다.

2. itertools 모듈 사용
```python
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
```
---
</div>
</details>


<details>
<summary>035. 조합</summary>
<div markdown='1'>

---
1. DFS로 k개 조합 생성
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        
        dfs([], 1, k)
        return results
```

2. itertools 모듈 사용
```python
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))
```
---
</div>
</details>


<details>
<summary>036. 조합의 합</summary>
<div markdown='1'>

---
1. DFS로 중복 조합 그래프 탐색
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            
            if csum == 0:
                result.append(path)
                return
            
            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
            
        dfs(target, 0, [])
        return result
```

---
</div>
</details>


<details>
<summary>037. 부분 집합</summary>
<div markdown='1'>

---
0. 내 풀이
```python
# 내 풀이
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(subset):
            
            result.append(subset)

            for num in nums:
                if not subset or subset[-1] < num:
                    dfs(subset + [num])

        dfs([])
        return result
```
- ```subset```이 비어있거나 ```subset```의 마지막 원소가 다음으로 입력 될 원소보다 작아야한다.


1. 트리의 모든 DFS 결과
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return result
```
- 모든 탐색의 경로가 결국 정답이 되므로, 탐색할 때마다 매번 결과를 추가해주면 된다.
- ```dfs(i + 1, path + [nums[i]])``` 부분과 나의 코드 중 ```subset[-1] < num:``` 부분을 변경할 수 있다.

---
</div>
</details>


<details>
<summary>038. 일정 재구성</summary>
<div markdown='1'>

---
1. DFS로 일정 그래프 구성
```python
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def DFS(start):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[start]:
                DFS(graph[start].pop(0))
            route.append(start)

        DFS("JFK")

        # 다시 뒤집어서 어휘순 결과로
        return route[::-1]
```

2. 스택 연산으로 큐 연산 최소화
```python
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        def DFS(start):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[start]:
                DFS(graph[start].pop())
            route.append(start)

        DFS("JFK")

        # 다시 뒤집어서 어휘순 결과로
        return route[::-1]
```

3. 일정 그래프 반복
```python
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route, stack = [], ["JFK"]
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        
        # 다시 뒤집어서 어휘순 결과로
        return route[::-1]
```

---
</div>
</details>


<details>
<summary>039. 코드 스케쥴</summary>
<div markdown='1'>

---

---
</div>
</details>