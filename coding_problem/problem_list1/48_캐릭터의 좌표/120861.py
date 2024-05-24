# https://school.programmers.co.kr/learn/courses/30/lessons/120861
# Pass

def solution(keyinput, board):
    answer = []
    board_mid = (board[0] - 1) // 2
    
    mid_x = (board[0] - 1) // 2
    mid_y = (board[1] - 1) // 2
    
    start = [0, 0]
    for key in keyinput:
        cx, cy = start[0], start[1]
        
        if key == 'left':
            nx, ny = cx - 1, cy
            if -mid_x <= nx <= mid_x and -mid_y <= ny <= mid_y:
                start = [nx, ny]
        
        elif key == 'right':
            nx, ny = cx + 1, cy
            if -mid_x <= nx <= mid_x and -mid_y <= ny <= mid_y:
                start = [nx, ny]
        
        elif key == 'up':
            nx, ny = cx, cy + 1
            if -mid_x <= nx <= mid_x and -mid_y <= ny <= mid_y:
                start = [nx, ny]
        
        elif key == 'down':
            nx, ny = cx, cy - 1
            if -mid_x <= nx <= mid_x and -mid_y <= ny <= mid_y:
                start = [nx, ny]
                
    return start
