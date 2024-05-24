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