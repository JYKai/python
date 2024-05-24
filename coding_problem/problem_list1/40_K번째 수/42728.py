def solution(array, commands):
    answer = []
    for command in commands:
        s, e, k = command
        temp = array[s-1: e]
        temp.sort()
        answer.append(temp[k - 1])
    return answer
