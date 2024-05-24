# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0] * 3
    
    for idx, a in enumerate(answers):
        if a == patterns[0][idx % len(patterns[0])]: scores[0] += 1
        if a == patterns[1][idx % len(patterns[1])]: scores[1] += 1
        if a == patterns[2][idx % len(patterns[2])]: scores[2] += 1
    
    maxi = max(scores)
    results = []
    for idx, score in enumerate(scores, start=1):
        if score == maxi: results.append(idx)
        
    return results