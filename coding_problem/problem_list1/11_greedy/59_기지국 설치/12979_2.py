import math

def solution(n, stations, w):
    answer = 0
    
    start = 1
    for station in stations:
        need_to_fill = (station - w) - start
        answer += math.ceil(need_to_fill / (w * 2 + 1))
        start = station + w + 1
        
    if start <= n:
        need_to_fill = (n - start) + 1
        answer += math.ceil(need_to_fill / (w * 2 + 1))
        
    return answer