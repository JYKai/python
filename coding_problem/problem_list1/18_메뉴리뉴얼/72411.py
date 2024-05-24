# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations, permutations

def solution(orders, course):
    answer = []
    # full = {}
    for c in course:
        full = {}
        for order in orders:
            combi_order = list(combinations(sorted(order), c))
            for combi in combi_order:
                if ''.join(combi) not in full:
                    full[''.join(combi)] = 0
                full[''.join(combi)] += 1
        
        for k, v in full.items():
            if v >= 2 and v == max(full.values()):
                answer.append(k)   
                
    # answer.sort()
    return answer