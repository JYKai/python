def solution(n, stations, w):
    answer = 0
    location = 1 # 현재 탐색하는 아파트의 위치
    idx = 0 # 설치된 기지국의 인덱스
    
    while location <= n:
        # 기지국이 설치된 위치에 도달할 경우
        if idx < len(stations) and location >= stations[idx] - w:
            location = stations[idx] + w + 1
            idx += 1
        # 기지국이 설치되지 않은 위치인 경우
        else:
            location += 2 * w + 1 # 기지국을 설치하고 해당 범위를 넘어감
            answer += 1
            
    return answer
