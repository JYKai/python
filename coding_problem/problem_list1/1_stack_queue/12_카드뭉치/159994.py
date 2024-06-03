# https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            cards1.popleft()
            answer += word
        
        elif len(cards2) > 0 and cards2[0] == word:
            cards2.popleft()
            answer += word
        
        else:
            break
    
    if answer == "".join(goal):
        return "Yes"
    else:
        return "No"