# 선형 자료구조(Linear Structure)
데이터 요소가 순차적으로 배열되는 자료구조를 선형 자료구조라고 한다.
- 선형 자료구조는 단일 레벨로 구성되기 때문에 한 번에 탐색이 가능하며, 구현이 쉽다.
- 배열, 스택, 큐, 연결 리스트 등이 모두 선형 자료구조에 속한다.

## 배열(Array)
일반적으로 배열이란 고정된 크기만큼의 연속된 메모리 할당이다. 하지만, 실제 데이터에서는 전체 크기를 가늠하기 힘들 때가 많기 때문에 자동으로 크기를 리사이징하는 배열인 동적 배열을 대부분의 프로그래밍 언어에서 지원한다.

### Problems

<details>
<summary>007. 두 수의 합</summary>
<div markdown='1'>

---
1. 브루드 포스(Brute-Force)로 계산
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

```
- 2중 for문을 통한 완전탐색
- 시간복잡도가 크다.

2. in을 이용한 탐색
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i+1: ]:
            return [nums.index(n), nums[i+1: ].index(complement) + (i + 1)]
```
- 모든 조합을 비교하지 않고 정답에서 첫 번째 뺀 값 target - n이 존재하는 지 탐색한다.
- 2중 for문을 통한 완전탐색보다 더 훨씬 더 빨리 동작한다.

3. 첫 번째 수를 뺀 결과 키 조회
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
```
- 딕셔너리로 저장하여 조회할 때에 발생하는 시간복잡도를 줄인다.

4. 조회 구조 개선
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
```

5. 투 포인터 이용
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_nums = [[num, idx] for idx, num in enumerate(nums)]
        idx_nums.sort(key=lambda x: x[0])
        
        left, right = 0, len(nums) - 1
        while left < right:
            if idx_nums[left][0] + idx_nums[right][0] == target:
                return [idx_nums[left][1], idx_nums[right][1]]
            elif idx_nums[left][0] + idx_nums[right][0] < target:
                left += 1
            else:
                right -= 1
```
- 투 포인터를 이용하기 위해 정렬이 필요하다는 점을 확인하고, 정렬로 인해 발생하는 인덱스 섞임에 대응한다. 
---
</div>
</details>


<details>
<summary>008. 빗물 트래핑</summary>
<div markdown='1'>

---
1. 투 포인터를 최대로 이동
```python
def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        # 더 높은 쪽을 향해 투 포인터 이동
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume
```
- 가장 높이가 높은 막대를 찾아본다. 막대의 높고 낮음과는 무관하게 해당 막대는 그저 왼쪽과 오른쪽을 가르는 장벽 역할을 해준다.
- 좌우 기둥 최대 높이가 현재 높이와의 차이만큼 물 높이를 더해준다.

2. 스택 쌓기
```python
def trap(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()
            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume
```
- 스택을 쌓으면서 현재 높이가 이전 높이보다 높을 때, 즉 꺽이는 부분 변곡점을 기준으로 격차만큼 물 높이를 채워준다.
---
</div>
</details>


<details>
<summary>009. 세 수의 합</summary>
<div markdown='1'>

---
1. 투 포인터로 합 계산
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
                
    return results
```
- i의 지점을 고정해둔 뒤, i + 1 부터 마지막 지점까지의 범위에서 투 포인터를 활용하여 합을 계산한다.
- 포인터의 양옆이 동일한 값이 있을 수 있으므로 반복해서 스킵처리 해준다.
---
</div>
</details>


<details>
<summary>010. 배열 파티션</summary>
<div markdown='1'>

---
1. 오름차순 풀이
```python
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum
```
- 페어의 min()을 합산했을 때 최대를 만드는 것은 결국 min()이 되도록 커야 한다는 뜻이기 때문에 오름차순으로 정렬하여 접근한다.

2. 짝수 번째 값 계싼
```python
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    
    return sum
```
- 정렬된 상태에서는 짝수 번째에 항상 작은 값이 위치하기 때문에 짝수 번째 값을 더하면 된다.

3. 파이썬다운 방식
```python
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
```
- 슬라이싱 구문[::2]을 사용해서 짝수 번째를 계산한다.
---
</div>
</details>


<details>
<summary>011. 자신을 제외한 배열의 곱</summary>
<div markdown='1'>

---
1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] *= p
            p *= nums[i]
            
        return out
```
---
</div>
</details>


<details>
<summary>012. 주식을 사고팔기 가장 좋은 시점</summary>
<div markdown='1'>

---
1. 저점과 현재 값과의 차이 계산
```python
import sys

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit
```
---
</div>
</details>

</br>
</br>

## 연결 리스트(Linked list)
연결 리스트는 데이터 요소의 선형 집합으로, 데이터의 순서가 메모리에 물리적인 순서대로 저장되지 않는다.
- 동적으로 새로운 노드를 삽입하거나 삭제하기 간편하며, 관리가 쉽다. = O(1)
- 특정 인덱스에 접근하기 위해서는 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. = O(n)

### Problems
<details>
<summary>013. 팰린드롬 연결 리스트</summary>
<div markdown='1'>

---
1. 리스트 변환
```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    q: List = []

    if not head:
        return True
    
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True
```
- 연결 리스트 입력값을 파이썬의 리스트로 변환하여 풀이

2. Deque를 이용한 최적화
```python
from collections import deque

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    q: Deque = deque()

    if not head:
        return True
    
    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True
```

3. 런너를 이용한 풀이
```python
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head
    
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next # 다중 할당
    
    if fast:
        slow = slow.next
    
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev
```
- 속도가 다른 두 런너를 설정해서 빠른 런너가 끝에 도달했을 때, 느린 런너가 정확히 중간 지점에 도달하게 한다.
- 느린 런너는 역순으로 연결 리스트를 만든다. 빠른 런너가 도착했을 때, 느린 런너는 나머지 이동 경로와 역순으로 만든 연결 리스트를 비교한다.
---
</div>
</details>


<details>
<summary>014. 두 정렬 리스트의 병합</summary>
<div markdown='1'>

---
1. 재귀 구조로 연결
```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if (not list1) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1
    if list1:
        list1.next = self.mergeTwoLists(list1.next, list2)
    return list1
```
- 먼저, list1과 list2의 값을 비교해 작은 값이 왼쪽에 오게 하고, next는 그다음 값이 엮이도록 재귀 호출한다.
---
</div>
</details>


<details>
<summary>015. 역순 연결 리스트</summary>
<div markdown='1'>

---
1. 재귀 구조로 뒤집기
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)
```
- 다음 노드 next와 현재 노드 node를 파라미터로 지정한 함수를 재귀 호출한다.
- node.next에는 이전 prev 리스트를 계속 연결해주면서 node가 None이 될 때까지 재귀호출하면 마지막에는 백트래킹되면서 연결 리스트가 거꾸로 연결된다.

2. 반복 구조로 뒤집기
```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev
```
---
</div>
</details>


<details>
<summary>016. 두 수의 덧셈</summary>
<div markdown='1'>

---
1. 자료형 변환
```python
# 연결 리스트 뒤집기
def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev

# 연결 리스트를 파이썬 리스트로 변환
def toList(self, node: List) -> List:
    to_list: List = []
    while node:
        to_list.append(node.val)
        node = node.next
    return to_list

# 파이썬 리스트를 연결 리스트로 변환
def toReversedLinkedList(self, result: str) -> ListNode:
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node

# 두 연결 리스트의 덧셈
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    a = self.toList(self.reverseList(l1))
    b = self.toList(self.reverseList(l2))

    resultStr = int(''.join(str(e) for e in a)) + \
                int(''.join(str(e) for e in b))
            
    # 최종 계산 결과 연결 리스트 반환
    return self.toReversedLinkedList(str(resultStr))
```
- 역순으로 된 연결 리스트를 뒤집는다.
- 연결 리스트를 파이썬 리스트로 변환한다.
- 파이썬 리스트를 연결 리스트로 변환한다.

2. 전가산기(Full Adder) 구현
```python
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        
        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next
    
    return root.next
```

---
</div>
</details>


<details>
<summary>017. 페어의 노드 스왑</summary>
<div markdown='1'>

---
1. 값만 교환
```python
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head
```

2. 반복 구조로 스왑
```python
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next
    
    return root.next
```

3. 재귀 구조로 스왑
```python
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head
```

---
</div>
</details>


<details>
<summary>018. 홀짝 연결 리스트</summary>
<div markdown='1'>

---
1. 반복 구조로 홀짝 노드 처리
```python
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 예외 처리
    if head is None:
        return None
    
    odd = head
    even = head.next
    even_head = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    
    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head
```
---
</div>
</details>


<details>
<summary>019. 역순 연결 리스트2</summary>
<div markdown='1'>

---
1. 반복 구조로 노드 뒤집기
```python
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # 예외 처리
    if not head or left == right:
        return head
    
    root = start = ListNode(None)
    root.next = head

    # start, end 지정
    for _ in range(left - 1):
        start = start.next
    end = start.next

    # 반복하면서 노드 차례대로 뒤집기
    for _ in range(right - left):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next
```

---
</div>
</details>