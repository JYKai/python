# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    zero_cnt = 0
    bin_cnt = 0
    
    while len(s) != 1:
        num_zeros = s.count('0')
        modified_s = len(s) - num_zeros
        s = bin(modified_s)[2:]
        
        zero_cnt += num_zeros
        bin_cnt += 1
        
    return [bin_cnt, zero_cnt]
