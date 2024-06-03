# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    # [[0,0,0,0,0],
    #  [0,0,1,0,3],
    #. [0,2,5,0,1],
    #. [4,2,4,4,2],
    #. [3,5,1,3,1]]
    
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            # 1 -> 11, 21, 31, 41, 51
            temp = board[i][move - 1]
            # print("temp = ", temp)
            if temp != 0:
                # board[i][move - 1] = 0
                if stack and stack[-1] == temp:
                    # print("stack = ", stack)
                    # print("temp = ", temp)
                    stack.pop()
                    answer += 2
                else:
                    stack.append(temp)
                board[i][move - 1] = 0
                break
    return answer