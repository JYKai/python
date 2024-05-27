# 문자열 조작(String Manipulation)
문자열을 변경하거나 분리하는 등의 여러 과정

- 정보 처리 분야
- 통신 시스템 분야
- 프로그래밍 시스템 분야

## Problems


<details>
<summary>001. 유효한 팰린드롬</summary>
<div markdown='1'>

---
1. 리스트로 변환
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = []
        for word in s:
            if word.isalnum():
                alnum.append(word.lower())
        
        if alnum == alnum[::-1]:
            return True
        else:
            return False
```
- ```isalnum()```는 영문자, 숫자 여부를 판별하는 함수
- ```lower()```는 소문자로 변환해주는 함수
- 문자열 슬라이싱 ```alnum[::-1]```
    - 대부분의 문자열 작업은 슬라이싱으로 처리하는 편이 가장 빠르다.

2. Deque 자료형을 이용한 최적화
```python
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
```
---

</div>
</details>


<details>
<summary>002. 문자열 뒤집기</summary>
<div markdown='1'>

---
1. 투 포인터를 이용한 스왑
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

2. 파이썬다운 방식
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
```
- ```reverse()```는 리스트에만 제공한다.
- ```s[::-1]```으로 해결할 수 있으나, 이 문제에서는 공간 복잡도를 O(1)로 제한하기 때문에 변수 할당을 처리하는데 다소 제약이 있다.
    - ```s[:] = s[::-1]``` 와 같은 트릭을 사용하면 동작할 수 있다.
---
</div>
</details>


<details>
<summary>003. 로그 파일 재정렬</summary>
<div markdown='1'>

---
1. 람다와 + 연산자를 이용
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
```
- 문자와 숫자를 구분하거, 숫자는 나중에 그대로 이어 붙인다.
- 문자로그에서 식별자를 제외한 문자열[1:]을 키로 하여 정렬하며, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬되도록, 람다 표현식을 이용해 정렬한다.
---
</div>
</details>


<details>
<summary>004. 가장 흔한 단어</summary>
<div markdown='1'>

---
1. 리스트 컴프리헨션, Counter 객체 사용
```python
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                    if word not in banned]
        counts = Counter(words)

        return counts.most_common(1)[0][0]
```
- [정규표현식](https://wikidocs.net/4308)을 활용하여 데이터 전처리
    - ```\w``` : 단어 문자를 의미
    - ```^``` : not을 의미
---

</div>
</details>


<details>
<summary>005. 그룹 애너그램</summary>
<div markdown='1'>

---
1. 정렬하여 딕셔너리에 추가
```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
```
- ```sorted()```를 활용하여 문자열을 정렬하여, 이를 ```''.join()```으로 합쳐 딕셔너리의 키로 활용
- ```sort()```
    - 제자리 정렬(In-place Sort)라고 불린다. 제자리 정렬 알고리즘은 입력을 출력으로 덮어 쓰기 때문에 별도의 추가 공간이 필요하지 않고, 리턴값이 없다. ```sorted()```와 구분하자.
---

</div>
</details>


<details>
<summary>006. 가장 긴 팰린드롬 부분 문자열</summary>
<div markdown='1'>

---
1. 중앙을 중심으로 확장
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result, 
                            expand(i, i + 1),
                            expand(i, i + 2),
                            key=len)
        
        return result
```
- 투 포인터가 중앙을 중심으로 확장하는 형태
    - 투 포인터가 슬라이딩 윈도우처럼 계속 앞으로 전진하면서, 해당 부분의 문자열이 팰린드롬인 경우 멈추고, 점점 확장하는 방식
---

</div>
</details>