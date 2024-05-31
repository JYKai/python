from collections import deque

a = [1, 2, 3, 4, 5]
q = deque(a)

q.rotate(2) # 시계방향 회전은 양수, 그 반대는 음수

result = list(q)
print(result) # [4, 5, 1, 2, 3]