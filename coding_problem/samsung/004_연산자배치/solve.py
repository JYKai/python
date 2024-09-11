def DFS(L, current_result, add, sub, mul):
    global min_score, max_score

    if L == n:
        min_score = min(min_score, current_result)
        max_score = max(max_score, current_result)
        return
    
    if add > 0:
        DFS(L + 1, current_result + integers[L], add - 1, sub, mul)
    
    if sub > 0:
        DFS(L + 1, current_result - integers[L], add, sub - 1, mul)
    
    if mul > 0:
        DFS(L + 1, current_result * integers[L], add, sub, mul - 1)

n = int(input())
integers = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_score, max_score = float('inf'), -float('inf')

DFS(1, integers[0], operators[0], operators[1], operators[2])

print(min_score, max_score)