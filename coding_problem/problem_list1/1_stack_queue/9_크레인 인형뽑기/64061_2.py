from typing import List

def grep(board: List[List[int]], location: int) -> int:
    result = 0
    rows = len(board)
    
    for r in range(rows):
        doll = board[r][location]
        if doll == 0:
            continue
        else:
            result = doll
            board[r][location] = 0
            break
    
    return board, result
        

def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        board, doll = grep(board, move - 1)
        if not doll:
            continue
        if not stack or stack[-1] != doll:
            stack.append(doll)
        elif stack[-1] == doll:
            stack.pop()
            answer += 2
            
    return answer
