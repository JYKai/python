# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    remain = deque()
    for progress, speed in zip(progresses, speeds):
        remain_time = 100 - progress
        if remain_time % speed == 0:
            remain.append(remain_time // speed)
        else:
            remain.append(remain_time // speed + 1)
    
    cnt = 1
    while remain:
        cur = remain.popleft()
        while remain and remain[0] <= cur:
            remain.popleft()
            cnt += 1
        
        if len(remain) == 1:
            if cur > remain[0]:
                remain.popleft()
                cnt += 1
                
        answer.append(cnt)
        cnt = 1
        
    return answer