# 내 코드

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] == '(':
                    if i == ')':
                        stack.pop()
                    elif i in ['(', '{', '[']:
                        stack.append(i)
                    else:
                        return False
                
                elif stack[-1] == '{':
                    if i == '}':
                        stack.pop()
                    elif i in ['(', '{', '[']:
                        stack.append(i)
                    else:
                        return False

                elif stack[-1] == '[':
                    if i == ']':
                        stack.pop()
                    elif i in ['(', '{', '[']:
                        stack.append(i)
                    else:
                        return False
                        
        return True if not stack else False