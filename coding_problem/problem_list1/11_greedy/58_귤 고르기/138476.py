from collections import Counter

def solution(k, tangerine):
    tang_cnt = Counter(tangerine)
    tang_cnt = sorted(tang_cnt.values(), reverse=True)
    
    num_types = 0
    count_sum = 0
    
    for count in tang_cnt:
        count_sum += count
        num_types += 1
        
        if count_sum >= k:
            break
            
    return num_types
