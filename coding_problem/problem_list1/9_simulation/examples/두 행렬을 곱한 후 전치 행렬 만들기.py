
def multiply_matrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None

    multiplied_matrix = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                multiplied_matrix[i][j] += (matrix1[i][k] * matrix2[k][j])

    return multiplied_matrix

def transpose_matrix(matrix):
    row, col = len(matrix), len(matrix[0])
    transposed_matrix = [[0] * row for _ in range(col)]

    for r in range(row):
        for c in range(col):
            transposed_matrix[c][r] = matrix[r][c]

    return transposed_matrix


def solution(matrix1, matrix2):
    multiplied_matrix = multiply_matrix(matrix1, matrix2)
    transposed_matrix = transpose_matrix(multiplied_matrix)
    return transposed_matrix
    
print(solution(
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
],

[
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]))