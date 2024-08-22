from collections import Counter

def solution(N, stages):
    answer = []
    people = len(stages)

    stages_count = Counter(stages)
    for stage in range(1, N + 1):
        if stage not in stages_count:
            fail = 0
        else:   
            remain = stages_count[stage]
            fail = remain / people
            people -= remain
        answer.append([stage, fail])
    
    answer.sort(reverse=True, key=lambda x: x[1])

    return [stage for stage, fail in answer]
