# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    for word in s:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    return int(not stack)