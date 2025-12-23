N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

def is_row(cnt):
    result = 1
    num = -1
    count = 1

    for y in range(0, N):
        if maps[y][cnt] == num:
            count += 1
        else:
            num = maps[y][cnt]
            result = max(result, count)
            count = 1
    result = max(result, count)
    return result

def is_col(cnt):
    result = 1
    num = -1
    count = 1

    for x in range(0, N):
        if maps[cnt][x] == num:
            count += 1
        else:
            num = maps[cnt][x]
            result = max(result, count)
            count = 1
    result = max(result, count)
    return result

result = 0

for i in range(N):
    c = is_col(i)
    r = is_row(i)

    if c >= M:
        result += 1

    if r >= M:
        result += 1

print(result)