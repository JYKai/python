from collections import deque

def check(s):
    stack = []
    for p in s:
        if p in ['[', '{', '(']:
            stack.append(p)
        else:
            if not stack:
                return False
            if p == ']' and stack[-1] == '[':
                stack.pop()
            elif p == '}' and stack[-1] == '{':
                stack.pop()
            elif p == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return not stack

def solution(s):
    answer = 0
    n = len(s)
    s = deque(s)
    for i in range(n):
        s.rotate(-1) # deque()의 rotate 함수 활용
        if check(s):
            answer += 1
    return answer

