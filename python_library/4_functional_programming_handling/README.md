# 함수형 프로그래밍 다루기
함수형 프로그래밍(functional programming)은 자료 처리를 수학 함수 계산으로 취급하고 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임의 하나다.

<details>
<summary>023. 상담원을 순서대로 배정하려면?</summary>
<div markdown='1'>

---
**itertools.cycle(iterable)**  
반복 가능한 객체를 순서대로 무한히 반복하는 이터레이터를 생성하는 함수

> Q. 3명의 상담원이 돌아가면서 고객을 응대할 수 있도록 하는 방법은?
```python
import itertools

emp_pool = itertools.cycle(['김지윤', '이윤지', '박지은'])
for _ in range(10):
    print(next(emp_pool), end=', ') # 김지윤, 이윤지, 박지은, 김지윤, 이윤지 ...   
```
- ```itertools.cycle``` 함수로 무한히 반복하는 이터레이터를 생성한 뒤 ```next()```를 호출한다.

---
</div>
</details>


<details>
<summary>024. 연간 매출액을 계산하려면?</summary>
<div markdown='1'>

---
**itertools.accumulate(iterable)**  
반복 가능한 객체의 누적합을 계산하여 이터레이터로 반환하는 함수

> Q1. 월별 매출액의 누적합을 계산하는 방법은?
```python
import itertools

monthly_income = [1123, 1242, 5322, 1242, 3212, 5224, 6642, 3232, 2211, 2153]
result = list(itertools.accumulate(monthly_income))

print(result) # [1123, 2365, 7687, 8929, 12141, 17365, 24007, 27239, 29450, 31603]
```

> Q1-1. 그때까지의 최댓값 표시하는 방법은?
```python
result = list(itertools.accumulate(monthly_income, max))

print(result) # [1123, 1242, 5322, 5322, 5322, 5322, 6642, 6642, 6642, 6642]
```
- 두 번째 인수로 max를 전달하면 된다.

---
</div>
</details>
