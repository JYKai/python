# 수학과 숫자 다루기

<details>
<summary>017. 과자를 똑같이 나누어 담으려면?</summary>
<div markdown='1'>

---
**math.gcd**  
최대공약수(GCD, Greatest Common Divisor)를 쉽게 구할 수 있는 함수. 
- python 3.5버전부터 사용할 수 있다.
```python
import math

print(math.gcd(60, 100, 80)) # 20
```

---
</div>
</details>


<details>
<summary>018. 버스가 동시에 도착할 시간을 알려면?</summary>
<div markdown='1'>

---
**math.lcm()**  
최소 공배수(LCM, Least Common Multiple)을 구하는 함수
- python 3.9 버전부터 사용할 수 있다.

```python
import math

print(math.lcm(15, 25)) # 75
```
---
</div>
</details>


<details>
<summary>019. 소수점을 정확하게 계산하려면?</summary>
<div markdown='1'>

---
**decimal.Decimal**  
숫자를 10진수로 처리하여 정확한 소숫점 자릿수를 표현할 때 사용하는 모듈
- 이진수 기반의 파이썬 float 연산은 때에 따라 미세한 오차가 발생할 수 있다.
```python
0.1 * 3 # 0.300000000004
```

두 값이 가까운지를 확인하는 ```math.isclose()``` 함수를 이용하는 방법
```python
import math
math.isclose(0.1 * 3, 0.3) # True
```
- 완전한 해결책은 될 수 없다.

```python
from decimal import Decimal

print(Decimal('0.1') * 3) # 0.3
print(Decimal('1.2') - Decimal('0.1')) # 1.1
```
- 인수로 문자열을 사용해야 한다.
- Decimal 자료형은 다시 float 자료형으로 형변환할 수 있다.

```python
float(Decimal('0.1') * Decimal('0.1')) == 0.01 # True
```
- 정수연산은 가능하지만, 실수연산은 불가능하다.
- 고정 소수점을 사용하여 메모리를 많이 차지하므로 모든 float 연산을 Decimal로 바꾸는 것은 바람직하지 않다.
- 일반적으로 한 치의 오차도 허용하지 않는 금융권 또는 재무/회계 관련 프로그램을 작성할 때 사용하는 것이 좋다.
---
</div>
</details>
