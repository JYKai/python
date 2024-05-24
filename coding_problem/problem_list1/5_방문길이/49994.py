# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    check = set()
    cnt = 0
    
    x, y = 0, 0
    for d in dirs:
        if d == 'U':
            nx, ny = x, y + 1
        
        if d == 'L':
            nx, ny = x - 1, y
        
        if d == 'R':
            nx, ny = x + 1, y
        
        if d == 'D':
            nx, ny = x, y - 1
            
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if (x, y, nx, ny) not in check:
                cnt += 1
                check.add((x, y, nx, ny))
                check.add((nx, ny, x, y))
                
            x, y = nx, ny

    return cnt