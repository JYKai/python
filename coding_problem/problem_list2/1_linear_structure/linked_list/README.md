# 선형 자료구조(Linear Structure)
데이터 요소가 순차적으로 배열되는 자료구조를 선형 자료구조라고 한다.
- 선형 자료구조는 단일 레벨로 구성되기 때문에 한 번에 탐색이 가능하며, 구현이 쉽다.
- 배열, 스택, 큐, 연결 리스트 등이 모두 선형 자료구조에 속한다.

## 연결 리스트(Linked list)
연결 리스트는 데이터 요소의 선형 집합으로, 데이터의 순서가 메모리에 물리적인 순서대로 저장되지 않는다.
- 동적으로 새로운 노드를 삽입하거나 삭제하기 간편하며, 관리가 쉽다. = O(1)
- 특정 인덱스에 접근하기 위해서는 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. = O(n)

## Problems
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

</br>
