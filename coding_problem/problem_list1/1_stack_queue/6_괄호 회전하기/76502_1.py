# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def check(strings):
    stack = []
    for string in strings:
        if not stack:
            if string in ['}', ']', ')']:
                return False
            else:
                stack.append(string)
        else:
            if string == '}':
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            
            elif string == ']':
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            
            elif string == ')':
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(string)
    
    if not stack:
        return True
    else:
        return False

def solution(s):
    if len(s) == 1:
        return 0
    answer = 0
    strings = list(s)
    for i in range(len(s)):
        if check(strings):
            answer += 1
        strings.append(strings.pop(0))
    return answer