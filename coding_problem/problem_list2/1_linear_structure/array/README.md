# 선형 자료구조(Linear Structure)
데이터 요소가 순차적으로 배열되는 자료구조를 선형 자료구조라고 한다.
- 선형 자료구조는 단일 레벨로 구성되기 때문에 한 번에 탐색이 가능하며, 구현이 쉽다.
- 배열, 스택, 큐, 연결 리스트 등이 모두 선형 자료구조에 속한다.

## 배열(Array)
일반적으로 배열이란 고정된 크기만큼의 연속된 메모리 할당이다. 하지만, 실제 데이터에서는 전체 크기를 가늠하기 힘들 때가 많기 때문에 자동으로 크기를 리사이징하는 배열인 동적 배열을 대부분의 프로그래밍 언어에서 지원한다.

## Problems

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