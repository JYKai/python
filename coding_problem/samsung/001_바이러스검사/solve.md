## 문제 풀이
```python
import math

rest = int(input())
cust = list(map(int, input().split()))
ldr, mbr = map(int, input().split())

cnt = 0
for cus in cust:
    cus -= ldr
    cnt += 1

    if cus > 0:
        cnt += math.ceil(cus / mbr)

print(cnt)
```
- `math.ceil` 함수를 활용하여 더 편리하고 가독성 좋게 코드 작성!
- LDR 즉, 팀장을 먼저 처리하고 팀원을 처리하는 그리디 방법.