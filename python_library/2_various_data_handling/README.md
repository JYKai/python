# Various data handling
- datetime
    - 두 날짜의 차이나 특정 날짜의 요일을 쉽게 구할 수 있는 모듈
- calendar
    - 윤년 확인 가능
- collections
    - 튜플, 딕셔너리를 더 효과적으로 사용할 수 있는 모듈
- pprint
    - 데이터를 보기 좋게 출력하는 모듈

<details>
<summary>날짜를 계산하고 요일을 알려면?</summary>
<div markdown="1">

---
**datetime.data** 는 년, 월, 일로 날짜를 표현할 때 사용하는 모듈이다.

### 시간 계산
```python
import datetime

day1 = datetime.date(2023, 10, 12)
print(day1) # 2023-10-12

day2 = datetime.date(2024, 5, 24)
print(day2) # 2024-05-24

diff = day2 - day1
print(diff.days) # 225

# 시, 분, 초까지 계산
day3 = datetime.datetime(2024, 5, 24, 11, 00, 00)
print(day3.hour) # 11
print(day3.minute) # 0
print(day3.second) # 0

# datetime.date 객체 + datetime.time 객체
day = datetime.date(2024, 5, 24)
time = datetime.time(11, 5, 40)

dt = datetime.datetime.combine(day, time)
print(dt) # 2024-05-24 11:05:40
```

### 요일 알아내기
```python
import datetime

day = datetime.date(2024, 5, 24)
print(day.weekday()) # 4
```
- 0(월요일)을 시작으로 1, 2, 3, ..., 6(일요일)
- 1을 월요일로 시작하고 싶다면 ```isoweekday()```을 사용한다.
---

</div>
</details>

<details>
<summary>두 날짜의 차이를 알려면?</summary>
<div markdown='1'>

---
**datetime.timedelta()**
- 두 날짜의 차이를 계산할 때 사용하는 함수.

### 오늘부터 100일 후?
```python
import datetime

today = datetime.date.today()
print(today) # 2024-05-24

diff_days = datetime.timedelta(days=100)
print(diff_days) # 100 days, 0:00:00

# 100일 후
print(today + diff_days) # 2024-09-01

# 100일 전
print(today - diff_days) # 2024-02-14
```

---

</div>
</details>


<details>
<summary>2월 29일인 해를 알려면?</summary>
<div markdown='1'>

---
**calendar.isleap()**
- 인수로 입력한 연도가 윤년인지 확인할 때 사용하는 함수.

### 윤년을 정하는 규칙
1. 서력 기원 연수가 4로 나누어 떨어지는 해는 우선 윤년으로 한다.
2. 그중에서 100으로 나누어 떨어지는 해는 평년으로 한다.
3. 400으로 나누어 떨어지는 해는 다시 윤년으로 정한다.
```python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
```

```python
import calendar
print(calendar.isleap(0)) # True
print(calendar.isleap(4)) # True
print(calendar.isleap(700)) # False
print(calendar.isleap(1200)) # True
print(calendar.isleap(2024)) # True
```

---

</div>
</details>

<details>
<summary>앞뒤에서 자료를 넣고 빼려면?</summary>
<div markdown='1'>

---
**collections.deque**  
deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형이다.

리스트를 n만큼 회전하는 문제를 해결하기 위해 주로 사용된다.
```python
from collections import deque

a = [1, 2, 3, 4, 5]
q = deque(a)

q.rotate(2) # 시계방향 회전은 양수, 그 반대는 음수

result = list(q)
print(result) # [4, 5, 1, 2, 3]
```
---
- ```rotate()``` : 시계방향 회전은 양수, 그 반대는 음수
- ```appendleft()``` : 데크 왼쪽에 x 추가
- ```popleft()``` : 데크 왼쪽에서 요소를 제거
- 장점
    - deque는 list보다 속도가 빠르다. pop(0)과 같은 메서드를 수행할 때 리스트는 O(N) 연산을 수행하지만, deque는 O(1) 연산을 수행하기 때문이다.
    - 스레드 환경에서 안전하다.
</div>
</details>


<details>
<summary>자료에 이름을 붙이려면?</summary>
<div markdown='1'>

---
**collections.namedtuple**  
네임드 튜플은 인덱스뿐만 아니라 키(key)로도 데이터에 접근할 수 있는 자료형이다.

```python
from collections import namedtuple

data = [
    ('홍길동', 23, '01011111111'),
    ('김철수', 31, '01022222222'),
    ('이영희', 29, '01033333333')
]

# namedtuple 자료형 생성
Employee = namedtuple('Employee', 'name, age, cellphone')

# data = [Employee(emp[0], emp[1], emp[2]) for emp in data]
data = [Employee._make(emp) for emp in data]

emp = data[0]
print(emp.name, emp.age, emp.cellphone) # 홍길동 23 01011111111
print(emp._asdict()) # {'name': '홍길동', 'age': 23, 'cellphone': '01011111111'}

# emp.name = '박길동' -> 값 변경시 오류 발생
new_emp = emp._replace(name='박길동')
print(new_emp) # Employee(name='박길동', age=23, cellphone='01011111111')
```
- ```namedtuple()```
    - 첫 번째 입력 : 자료형 이름(type name)
    - 보통 ```namedtuple()```로 생성하는 객체 이름과 같도록 한다.
    - 나머지 입력 : 쉼표로 구성된 문자열은 해당 namedtuple의 속성이 된다.
- ```_make()```
    - 리스트 컴프리헨션을 통해 할당을 할 수 있지만, 튜플의 요소가 많다면 ```_make()``` 함수를 사용하는 것이 유리하다.
- ```_asdict()```
    - 딕셔너리로 변환할 수 있다.
- 네임드 튜플의 값은 튜플의 immutable 특징을 그대로 가지고 있기 때문에 속성값을 변경할 수 없다.
- ```_replace()```를 통해 값을 바꿀 수 있지만, 해당 함수는 객체를 직접 변경하는 것이 아닌 값을 변경한 새로운 객체를 만들어 반환한다는 점에 주의하자.
---
</div>
</details>

<details>
<summary>사용한 단어 개수를 구하려면?</summary>
<div markdown='1'>

---
**collections.Counter**  
리스트나 문자열과 같은 자료형의 요소 중 값이 같은 요소가 몇 개인지를 확인할 때 사용하는 클래스이다.

```python
from collections import Counter
import re

data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.

산에
산에
피는 꽃은
저만치 혼자서 피어있네.

산에서 우는 새여
꽃이 좋아
산에서
사노라네.

산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""

words = re.findall(r'\w+', data)
counter = Counter(words)

print(counter)
"""
Counter({'꽃이': 5, '피네': 3, '산에는': 2, '갈': 2, 
         '봄': 2, '산에': 2, '산에서': 2, '지네': 2, 
         '꽃': 1, '여름없이': 1, '피는': 1, '꽃은': 1, 
         저만치': 1, '혼자서': 1, '피어있네': 1, '우는': 1, 
         '새여': 1, '좋아': 1, '사노라네': 1, '꽃지네': 1, 
         '여름': 1, '없이': 1})
"""

print(counter.most_common(1)) # [('꽃이', 5)]
print(counter.most_common(2)) # [('꽃이', 5), ('피네', 3)]
```
- ```\w+``` : 단어를 의미
- ```most_common()```
    - 빈도수가 많은 것부터 인수로 입력한 개수만큼 튜플로 반환한다.
---
</div>
</details>


<details>
<summary>딕셔너리를 한 번에 초기화하려면?</summary>
<div markdown='1'>

---
**collections.defaultdict**  
값(value)에 초깃값을 지정하여 딕셔너리를 생성하는 모듈

```python
from collections import defaultdict

text = 'Life is too short, You need python.'

text_dict = defaultdict(int)
for key in text:
    text_dict[key] += 1

print(text_dict) # defaultdict(<class 'int'>, {'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 
                 # 's': 2, 't': 3, 'o': 5, 'h': 2, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 2, 'd': 1, 'p': 1, 'y': 1, '.': 1})
```
- 인수로 원하는 타입을 지정해주어 초기화 과정을 생략할 수 있다.

---
</div>
</details>


<details>
<summary>수상자 3명을 선정하려면?</summary>
<div markdown='1'>

---
**heapq**  
순위가 가장 높은 자료(data)를 가장 먼저 꺼내는 우선순위 큐를 구현한 모듈

```python
import heapq

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

## 방법 1
# h = [] # 힙 생성
# for score in data:
#     heapq.heappush(h, score) # 힙에 데이터 저장

## 방법 2
heapq.heapify(data)

for i in range(3):
    print(heapq.heappop(h)) # (11.57, '차동현'), (11.67, '차정웅'), (11.92, '한시우')
```
- ```heappush()```로 튜플을 추가할 때는 데이터의 우선순위를 나타내는 항목이 첫 번째여야 한다.
- ```heapify()``` 함수로 data 리스트를 힙으로 만들 수 있다. 다만, data 리스트가 힙 구조에 맞게 변경된다.

```python
print(heapq.nsmallest(3, data))
```
- ```nsmallest(n, iterable)```
    - 반복 가능한 객체 데이터 집합에서 n개의 가장 작은 요소로 구성된 리스트를 반환한다.

---
</div>
</details>


<details>
<summary>데이터를 보기 좋게 출력하려면?</summary>
<div markdown='1'>

---
**pprint**  
데이터를 보기 좋게 출력(pretty print)할 때 사용하는 모듈

```python
from pprint import pprint

data = {'userId': 1, 'id': 1, 'title': 'sunt aur aksd sdlkajlj fdlksjf sldksdfkl sdlfkjsl',
        'body': 'aksdadnaskdnas asdjals asdkjas lk alioa ioas diojaoakdnla aslkdnassadaks'}

pprint(data)

'''
{'body': 'aksdadnaskdnas asdjals asdkjas lk alioa ioas diojaoakdnla '
         'aslkdnassadaks',
 'id': 1,
 'title': 'sunt aur aksd sdlkajlj fdlksjf sldksdfkl sdlfkjsl',
 'userId': 1}
'''
```
- 복잡한 데이터를 보기 좋게 출력할 수 있다.
- 구조가 복잡한 JSON 데이터를 디버깅 용도로 출력할 때 pprint를 자주 사용한다.

---
</div>
</details>
