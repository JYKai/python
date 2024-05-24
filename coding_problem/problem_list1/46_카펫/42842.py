# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math

def solution(brown, yellow):
    total = brown + yellow
    limit = int(math.sqrt(total))

    for num in range(3, limit + 1):
        if total % num == 0:
            m = total // num
            if (m - 2) * (num - 2) == yellow:
                return [m, num]
        
