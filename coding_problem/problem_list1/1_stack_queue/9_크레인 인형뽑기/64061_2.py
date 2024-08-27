from typing import List

def grep(board: List[List[int]], location: int) -> int:
    rows = len(board)
    
    for r in range(rows):
        doll = board[r][location]
        if doll != 0:
            board[r][location] = 0
            return doll
    
    return 0
        

def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        doll = grep(board, move - 1)
        if not doll:
            continue
        if stack and stack[-1] == doll:
            stack.pop()
            answer += 2
        else:
            stack.append(doll)
            
    return answer
