# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    p_dict = {}
    for p in participant:
        if p not in p_dict:
            p_dict[p] = 0
        p_dict[p] += 1
    
    for c in completion:
        p_dict[c] -= 1
    
    for k, v in p_dict.items():
        if v != 0: return k