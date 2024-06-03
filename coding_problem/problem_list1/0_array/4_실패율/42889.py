# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    # 1. 스테이지별 도전자 수를 구함
    challenger = [0] * (N + 2)
    for stage in stages:
        challenger[stage] += 1
    
    # 2. 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)
    
    # 3. 각 스테이지를 순회하며, 실패율 계산
    for i in range(1, N + 1):
        if challenger[i] == 0: # 4. 도전한 사람이 없는 경우, 실패율은 0
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total # 5. 실패율 구함
            total -= challenger[i] # 6. 다음 스테이지 실패율을 구하기 위해 현재 스테이지의 인원을 뺌
    
    # 7. 실패율이 높은 스테이지부터 내림차순으로 정렬
    print(fails)
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    
    return result