# 스택 & 큐(Stack & Queue)
## 스택
스택은 다음과 같은 두 가지 주요 연산을 지원하는 요소의 컬렉션으로 사용되는 추상 자료형(Abstract Data Type, ADT)이다.
- push(): 요소를 컬렉션에 추가한다.
- pop(): 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거한다.

</br>

## 큐
큐는 시퀀스의 한쪽 끝에는 엔티티를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션이다.

</br>

## Problems
<details>
<summary>020. 유효한 괄호</summary>
<div markdown='1'>

---
1. 스택 일치 여부 판별
```python
def isValid(self, s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    
    return len(stack) == 0
```
---
</div>
</details>


<details>
<summary>021. 중복문자 제거</summary>
<div markdown='1'>

---
1. 재귀를 이용한 분리
```python
def removeDuplicateLetters(self, s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char): ]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''
```
- lexicographical order: 사전에서 가장 먼저 찾을 수 있는 순서
- 중복 문자를 제외한 알파벳 순으로 문자열 입력값을 모두 정렬한 다음, 가장 빠른 접미사 a부터 접미사 suffix를 분리하여 확인한다.

2. 스택을 이용한 문자 제거
```python
from collections import Counter
def removeDuplicateLetters(self, s: str) -> str:
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)
```
- 만일 현재 문자 char가 스택에 쌓여 있는 문자(이전 문자보다 앞선 문자)이고, 뒤에 다시 붙일 문자가 남아 있다면(카운터가 0 이상이라면), 쌓아둔 걸 꺼내서 없앤다.
---
</div>
</details>


<details>
<summary>022. 일일온도</summary>
<div markdown='1'>

---
1. 스택 값 비교
```python
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = []
    for i, cur in enumerate(temperatures):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer
```
---
</div>
</details>


<details>
<summary>023. 큐를 이용한 스택 구현</summary>
<div markdown='1'>

---
1. push()할 때 큐를 이용해 재정렬
```python
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 매 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
```
---
</div>
</details>


<details>
<summary>024. 스택을 이용한 큐 구현</summary>
<div markdown='1'>

---
1. 스택 2개 사용
```python
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
    
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []
```
---
</div>
</details>


<details>
<summary>025. 원형 큐 디자인</summary>
<div markdown='1'>

---
1. 배열을 이용한 풀이
```python
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
    
    # enQueue(): rear 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
    
    # deQueue(): front 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
    
    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]
    
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None
    
    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
```
---
</div>
</details>