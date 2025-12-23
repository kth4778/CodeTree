from collections import deque

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]


def find(y, x):
    count = 0
    k = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[y][x] = True
    que = deque()
    que.append([y, x])
    result = 0

    if maps[y][x]:
        count = 1
        result = 1

    while (is_bool(visited)):
        k += 1

        for _ in range(len(que)):
            y, x = que.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append([ny, nx])

                    if maps[ny][nx] == 1:
                        count += 1

        if (k ** 2 + (k + 1) ** 2) <= count * M:
            result = max(count, result)
    return result

def is_bool(visited):
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False:
                return True
    return False

result = 0

for i in range(N):
    for j in range(M):
        result = max(result, find(i, j))

print(result)