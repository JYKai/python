"https://www.acmicpc.net/problem/16236"

from collections import deque

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

shark_point = [0, 0]
for i in range(N):
        for j in range(N):
                if maps[i][j] == 9:
                        shark_point[0], shark_point[1] = i, j

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def BFS(x, y):
        q = deque()
        q.append((x, y))

        visited = [[0] * N for _ in range(N)]
        visited[x][y] = 1

        fish_list = []

        while q:
                cx, cy = q.popleft()
                for i in range(4):
                        nx, ny = cx + dx[i], cy + dy[i]
                        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                                if maps[nx][ny] != 0 and maps[nx][ny] < maps[x][y]:
                                        visited[nx][ny] = visited[cx][cy] + 1
                                        fish_list.append((visited[nx][ny] - 1, nx, ny))

                                elif maps[nx][ny] == maps[x][y] or maps[nx][ny] == 0:
                                        visited[nx][ny] = visited[cx][cy] + 1
                                        q.append((nx, ny))

        return sorted(fish_list, key=lambda x: (x[0], x[1], x[2]))

shark = [2, 0]
x, y = shark_point[0], shark_point[1]
cnt = 0

while True:
        maps[x][y] = shark[0]
        fish_list = deque(BFS(x, y))

        if not fish_list:
                break

        step, cx, cy = fish_list.popleft()
        cnt += step
        shark[1] += 1

        if shark[0] == shark[1]:
                shark[0] += 1
                shark[1] = 0

        maps[x][y] = 0
        x, y = cx, cy

print(cnt)

