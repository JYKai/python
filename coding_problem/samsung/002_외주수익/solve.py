def dfs(L, money, work):
    global answer, n

    if L >= n:
        answer = max(answer, money)
        return

    t, p = work[L]
    if L + t <= n:
        dfs(L + t, money + p, work)
    dfs(L + 1, money, work)

n = int(input())

work = []
for _ in range(n):
    t, p = map(int, input().split())
    work.append([t, p])

answer = 0
dfs(0, 0, work)

print(answer)