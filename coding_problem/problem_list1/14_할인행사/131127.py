# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    want_dict = {}
    for w, n in zip(want, number):
        want_dict[w] = n
    
    cnt = 0
    for i in range(len(discount) - 9):
        discount_list = {}
        for j in range(i, i + 10):
            if discount[j] in want_dict:
                discount_list[discount[j]] = discount_list.get(discount[j], 0) + 1
                
        if discount_list == want_dict:
            cnt += 1
            
    return cnt