from collections import Counter, defaultdict

def solution(want, number, discount):
    answer = 0
    want_number = {w: n for w, n in zip(want, number)}
    init = dict(Counter(discount[:10]))
    
    for i in range(len(discount) - 9):
        if init == want_number:
            answer += 1
        if i + 10 < len(discount):
            init[discount[i]] -= 1
            if init[discount[i]] == 0:
                del init[discount[i]]
            init[discount[i + 10]] = init.get(discount[i + 10], 0) + 1
            
    return answer
