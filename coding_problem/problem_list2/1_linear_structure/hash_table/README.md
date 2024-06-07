# 해시 테이블
해시 테이블 또는 해시 맵은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형(ADT)을 구현한 자료구조다.
- 대부분의 연산이 분할 상관 분석에 따른 시간 복잡도기 O(1)이다.

## 해시
해시 함수란 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수를 말한다.  

**해싱(Hashing)**  
해시 테이블을 인덱싱하기 위해 해시 함수를 사용하는 것
- 충돌을 최소화하는 일이 무엇보다 중요.

</br>

## 충돌(Collision)

### 개별 체이닝(Seprate Chaining)
충돌 발생 시 연결 리스트로 연결하는 방식
- 구현이 잘 된 경우 대부분의 탐색은 O(1), 최악의 경우, 즉 모든 해시 충돌이 발생했을 경우 O(n)

### 오픈 어드레싱(Open Addressing)
충돌 발생 시 탐사(Probing)를 통해 빈 공간을 찾아나서는 방식
- 개별 체이닝과 달리 모든 원소가 자신의 해시값과 일치하는 주소에 저장된다는 보장은 없다.
- 버킷 사이즈보다 큰 경우에는 삽입할 수 없다.
    - 로드 팩터 비율을 넘어서게 되면, 그로스 팩터(Growth Factor)의 비율에 따라 더 큰 크기의 또 다른 버킷을 생성한 후 새롭게 복사하는 리해싱(Rehasing) 작업이 일어난다.

**선형 탐사(Linear Probing)**  
충돌이 발생할 경우 해당 위치부터 순차적으로 탐사하는 방식
- 간단하지만, 저장되는 데이터들이 고르게 분포되지 않고 뭉치는 경향(Clustering)이 있다.

### 파이썬의 해시 테이블 충돌 방식
**오픈 어드레싱**  
- 체이닝 시 malloc으로 메모리를 할당하는 오버헤드가 높아 오픈 어드레싱을 택했다.
- 연결 리스트를 만들기 위해서는 추가 메모리 할당이 필요하고, 추가 메모리 할당은 상대적으로 느린 작업이다.

</br>

## Problems

<details>
<summary>028. 해시맵 디자인</summary>
<div markdown='1'>

---
1. 개별 체이닝 방식을 이용한 헤시 테이블 구현
```python
from collections import defaultdict

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000 # 적절히 설정
        self.table = defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인데스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    
    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
            
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```
---
</div>
</details>


<details>
<summary>029. 보석과 돌</summary>
<div markdown='1'>

---
1. 해시 테이블을 이용한 풀이
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # 돌(stones)의 빈도 수 계산
        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        # 보석(jewels)의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count
```

2. 파이썬다운 방식
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
```
- ```[s for s in stons]``` = ['a', 'A', 'A', 'b', 'b', 'b']
- ```[s in jewels for s in stones]``` = [True, True, True, False, False, False, False]
- ```sum(s in jewels for s in stones)``` = 3
---
</div>
</details>


<details>
<summary>030. 중복 문자 없는 가장 긴 부분 문자열</summary>
<div markdown='1'>

---
1. 슬라이딩 윈도우와 투 포인터로 사이즈 조절
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)
        
            # 현재 문자의 위치 삽입
            used[char] = index
            
        return max_length
```
- 투 포인터로 문제를 풀이하되, 포인터 2개 모두 왼쪽에서 출발한다.
    - index : 우측 포인터
- ```start <= used[char]```
    - 현재 슬라이딩 위도우 바깥에 있는 문자는 예전에 등장한 적이 있더라도 지금은 무시해야 한다,
---
</div>
</details>


<details>
<summary>031. 상위 K 빈도 요소</summary>
<div markdown='1'>

---
1. Counter를 이용한 음수 순 추출
```python
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        topk = list()
        # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk
```

2. 파이썬 다운 방식
```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]
```

**```zip()```**  
- 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는 새로운 튜플 시퀀스를 만드는 역할을 한다.
- 튜플 시퀀스를 만들기 때문에 값을 변경하는게 불가능한다.

**아스테리스크(*)**  
- '*'은 언팩(Unpack)이다. 시퀀스를 풀어 헤치는 연산자를 뜻하며, 주로 튜플이나 리스트를 언패킹하는 데 사용한다.

---
</div>
</details>