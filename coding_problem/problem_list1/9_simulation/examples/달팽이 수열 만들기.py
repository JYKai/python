def check_possible(n, matrix, current_r, current_c, move, direction):
    next_r, next_c = current_r + move[direction][0], current_c + move[direction][1]
    if 0 <= next_r < n and 0 <= next_c < n and not matrix[next_r][next_c]:
        return True
    else:
        return False

def solution(n):
    snail_matrix = [[0] * n for _ in range(n)]
    start_r, start_c = 0, 0
    direction = 0
    move = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]
    for i in range(1, (n * n + 1)):
        if check_possible(n, snail_matrix, start_r, start_c, move, direction):
            snail_matrix[start_r][start_c] = i
            start_r += move[direction][0]
            start_c += move[direction][1]
        else:
            direction = (direction + 1) % 4
            snail_matrix[start_r][start_c] = i
            start_r += move[direction][0]
            start_c += move[direction][1]

    return snail_matrix

print(solution(5))