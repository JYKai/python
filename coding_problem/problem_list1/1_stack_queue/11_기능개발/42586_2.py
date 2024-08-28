from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    finish = deque()

    for progress, speed in zip(progresses, speeds):
        days = math.ceil((100 - progress) / speed)
        finish.append(days)

    first = finish.popleft()
    cnt = 1
    while finish:
        if finish[0] <= first:
            finish.popleft()
            cnt += 1
        else:
            answer.append(cnt)
            first = finish.popleft()
            cnt = 1

    answer.append(cnt)

    return answer
