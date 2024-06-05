def solution(N):
    result = []

    def DFS(num, sum_list):
        if sum(sum_list) == 10:
            result.append(sum_list)
            return

        if sum(sum_list) > 10:
            return

        if num == N + 1:
            return 
        
        DFS(num + 1, sum_list + [num])
        DFS(num + 1, sum_list)

    DFS(1, [])

    return result

print(solution(5))
print(solution(2))
print(solution(7))