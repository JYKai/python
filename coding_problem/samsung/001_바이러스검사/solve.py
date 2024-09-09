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