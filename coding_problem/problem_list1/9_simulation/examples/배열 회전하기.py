def rotate90(arr):
    row, col = len(arr), len(arr[0])
    temp = [[0] * col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            temp[r][c] = arr[row - 1 - c][r]
    return temp

def solution(arr, n):
    for _ in range(n):
        arr = rotate90(arr)

    return arr

print(solution(
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]
], 1))

print(solution(
[
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14,15,16]
 ], 2))