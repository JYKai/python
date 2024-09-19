def solution(board):
    nrow, ncol = len(board), len(board[0])
    dp = [[0] * ncol for _ in range(nrow)]
    
    max_square = 0
    for r in range(nrow):
        dp[r][0] = board[r][0]
        max_square = max(max_square, dp[r][0])
    for c in range(ncol):
        dp[0][c] = board[0][c]
        max_square = max(max_square, dp[0][c])
        
    for r in range(1, nrow):
        for c in range(1, ncol):
            if board[r][c] == 1:
                dp[r][c] = min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1]) + 1            
                max_square = max(max_square, dp[r][c])
                
    return max_square ** 2