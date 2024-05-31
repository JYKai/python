## 스택 & 큐(Stack & Queue)
### 스택
스택은 다음과 같은 두 가지 주요 연산을 지원하는 요소의 컬렉션으로 사용되는 추상 자료형(Abstract Data Type, ADT)이다.
- push(): 요소를 컬렉션에 추가한다.
- pop(): 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거한다.

</br>

### 큐
큐는 시퀀스의 한쪽 끝에는 엔티티를 추가하고, 다른 반대쪽 끝에는 제거할 수 있는 엔티티 컬렉션이다.

</br>

### Problems
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