# 백트래킹 & 백트래킹 알고리즘

## 백트래킹(backtracking)
어떤 가능성이 없는 곳을 알아보고 되돌아 가는 것

## 백트래킹 알고리즘
가능성이 없는 곳에서는 되돌아가고, 가능성이 있는 곳을 탐색하는 알고리즘

## 유망 함수
'해가 될 가능성을 판단하는 것'이 백트래킹 알고리즘의 핵심

**진행 과정**  
1. 유효한 해의 집합을 정의한다.
2. 위 단계에서 정의한 집합을 그래프로 표현한다.
3. 유망 함수를 정의한다.
4. 백트래킹 알고리즘을 활용해서 해를 찾는다.

## Problems
<details>
<summary>33. 피로도</summary>
<div markdown='1'>

---
1. 정답 풀이
```python
def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    visited = [False] * n
    
    def DFS(cnt, k):
        nonlocal answer
        
        answer = max(answer, cnt)
        
        for i in range(n):
            if not visited[i] and dungeons[i][0] <= k:
                visited[i] = True
                DFS(cnt + 1, k - dungeons[i][1])
                visited[i] = False
    
    DFS(0, k)
    return answer
```
**고민해야할 점**  
- 현재 피로도가 들어가려는 던전의 최소 피로도보다 높아야한다.
    - 현재 어떤 던전에 들어갈 수 있는지 선택할 때 영향을 미친다.
- 이후 해당 던전을 빠져나올 때 현재 피로도가 소모 피로도만큼 준다.
    - 현재 던전을 통과한 다음에 어떤 던전에 갈 수 있는지 선택할 때 영향을 미친다.

**유망 함수**  
- 현재 피로도가 최소 필요도보다 낮으면 백트래킹한다.
---
</div>
</details>


<details>
<summary>34. N-퀸</summary>
<div markdown='1'>

---
1. 내 풀이 (시간 초과!!)
```python
def is_col(c, maps):
    return 1 in (maps[i][c] for i in range(len(maps)))

def is_diag(r, c, maps):
    n = len(maps)
    for i in range(n):
        if r + i < n and c + i < n and maps[r + i][c + i] == 1:
            return True
        if r + i < n and c - i >= 0 and maps[r + i][c - i] == 1:
            return True
        if r - i >= 0 and c + i < n and maps[r - i][c + i] == 1:
            return True
        if r - i >= 0 and c - i >= 0 and maps[r - i][c - i] == 1:
            return True
        
    return False

def is_valid(r, c, maps):
    return not (is_col(c, maps) or is_diag(r, c, maps))

def solution(n):
    ans = 0
    maps = [[0] * n for _ in range(n)]
    
    def DFS(r):
        nonlocal ans
        if r == n:
            ans += 1
            return
        
        for c in range(n):
            if is_valid(r, c, maps):
                maps[r][c] = 1
                DFS(r + 1)
                maps[r][c] = 0
                    
    DFS(0)
    return ans
```

2. 정답 풀이
```python
# 1. 퀸이 서로 공격할 수 없는 위치에 놓이는 경우의 수를 구하는 함수
def getAns(n, y, width, diagonal1, diagonal2):
    ans = 0
    # 2. 모든 행에 대해서 퀸의 위치가 결정되었을 경우
    if y == n:
        # 3. 해결 가능한 경우의 수를 1 증가시킴
        ans += 1
    else:
        # 4. 현재 행에서 퀸이 놓일 수 있는 모든 위치를 시도
        for i in range(n):
            # 5. 해당 위치에 이미 퀸이 있는 경우, 대각선상에 퀸이 있는 경우 스킵
            if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
                continue
            # 6. 해당 위치에 퀸을 놓음
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = True
            # 7. 다음 행으로 이동하여 재귀적으로 해결 가능한 경우의 수 찾기
            ans += getAns(n, y + 1, width, diagonal1, diagonal2)
            # 8. 해당 위치에 놓은 퀸을 제거함
            width[i] = diagonal1[i + y] = diagonal2[i - y + n] = False
            
    return ans


def solution(n):
    ans = getAns(n, 0, [False] * n, [False] * (n * 2), [False] * (n * 2))
    return ans
```
**diagoanl1, 2: 체스판의 행과 열의 합을 이용하여 대각선을 체크하는 배열**    
- diagonal1: 오른쪽 위 -> 왼쪽 아래 방향 대각선 방향 퀸 중복 체크용 배열
- diagonal2: 왼쪽 위 -> 오른쪽 아래 방향 대각선 방향 퀸 중복 체크용 배열

---
</div>
</details>


<details>
<summary>35. 양궁대회</summary>
<div markdown='1'>

---
1. 정답 풀이
```python
from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    maxdiff, max_comb = 0, {}
    
    # 1. 주어진 조합에서 각각의 점수 계산
    def calculate_score(combi):
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10 - i] < combi.count(i):
                score1 += i
            elif info[10 - i] > 0: # >=가 아님을 주의!
                score2 += i
        return score1, score2
    
    # 2. 최대 차이와 조합 저장
    def calculate_diff(diff, cnt):
        nonlocal maxdiff, max_comb
        if diff > maxdiff:
            max_comb = cnt
            maxdiff = diff
    
    # 3. 가능한 라이언의 과녁 점수 조합의 모든 경우에 대해서 체크
    for combi in combinations_with_replacement(range(11), n):
        cnt = Counter(combi)
        score1, score2 = calculate_score(combi)
        diff = score1 - score2
        calculate_diff(diff, cnt)
    
    # 4. 최대 차이가 0 이상인 경우, 조합 반환
    if maxdiff > 0:
        answer = [0] * 11
        for n in max_comb:
            answer[10 - n] = max_comb[n]
        return answer
    else: # 최대 차이가 0인 경우, -1 반환
        return [-1]
    return answer
```
**문제의 핵심은 어떻게 해야 모든 경우를 빠지지 않고 체크할 수 있는지!**  
- 과녁을 맞힌 순서는 상관이 없으므로 조합으로 생각해야 한다. 순열은 순서에 의존.

**```from itertools import combinations_with_replacement```**  
- 백트래킹 류의 문제에서 자주 활용되는 함수 : 이터러블한 객체와 원소 개수를 받아 중복을 허용한 조합을 튜플 형태로 반환
- 중복을 허용하는 조합
---
</div>
</details>


<details>
<summary>36. 외벽점검</summary>
<div markdown='1'>

---
1. 정답 풀이
```python
from itertools import permutations

def solution(n, weak, dist):
    # 1. 주어진 weak 지점들을 선형으로 만들기 위해 weak 리스트에 마지막 지점 + n을 추가
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 2. 투입할 수 있는 친구들의 수에 1을 더한 값을 초깃값으로 설정
    answer = len(dist) + 1
    
    # 3. 모든 weak 지점을 시작점으로 설정하며 경우의 수 탐색
    for i in range(length):
        for friends in permutations(dist, len(dist)):
            # 4. friends에 들어 있는 친구들을 순서대로 배치하며 투입된 친구 수 측정
            cnt = 1
            position = weak[i] + friends[cnt - 1]
            # 5. 현재 투입된 친구가 다음 weak 지점까지 갈 수 있는지 검사
            for j in range(i, i + length):
                if position < weak[j]:
                    cnt += 1
                    # 6. 투입 가능한 친구의 수를 초과한 경우 탐색 중단
                    if cnt > len(dist):
                        break
                    position = weak[j] + friends[cnt - 1]
                
                # 7.최대 친구 수를 구함
                answer = min(answer, cnt)
    
    # 8. 모든 경우의 수를 탐색한 결과가 투입 가능한 친구 수를 초과하는 경우, -1 반환
    return answer if answer <= len(dist) else -1
```
- 친구들을 어떻게 배치하는지에 따라 모든 취약 지점을 방문하는 데 필요한 최소 친구 수가 다를 수 있으므로, 순열
- weak의 길이를 두 배로 늘려 시계 방향, 반시계 방향을 고려하지 않고 한 방향으로만 고려한다.

---
</div>
</details>


<details>
<summary>37. 사라지는 발판</summary>
<div markdown='1'>

---

---
</div>
</details>