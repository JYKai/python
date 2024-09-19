def solution(board):
    answer = 1
    row = len(board)
    col = len(board[0])
    
    for r in range(1, row):
        for c in range(1, col):
            if board[r][c] == 1:
                board[r][c] = min(board[r - 1][c], board[r][c - 1], board[r - 1][c - 1]) + 1
    
    answer = max(max(row) for row in board)

    return answer ** 2
