N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

def one(y, x):
    q = [[y, x], [y + 1, x], [y + 1, x + 1]]
    count = 0

    for y,x in q:
        if 0 <= y < N and 0 <= x < M:
            count += maps[y][x]
        else:
            return -1
        
    return count

def two(y, x):
    q = [[y, x + 1], [y + 1, x], [y + 1, x + 1]]
    count = 0

    for y,x in q:
        if 0 <= y < N and 0 <= x < M:
            count += maps[y][x]
        else:
            return -1
        
    return count

def three(y, x):
    q = [[y, x], [y + 1, x], [y, x + 1]]
    count = 0

    for y,x in q:
        if 0 <= y < N and 0 <= x < M:
            count += maps[y][x]
        else:
            return -1
        
    return count

def four(y, x):
    q = [[y, x], [y + 1, x + 1], [y, x + 1]]
    count = 0

    for y,x in q:
        if 0 <= y < N and 0 <= x < M:
            count += maps[y][x]
        else:
            return -1
        
    return count

def five(y, x):
    q = [[y, x], [y + 1, x], [y + 2, x]]
    count = 0

    for y,x in q:
        if 0 <= y < N and 0 <= x < M:
            count += maps[y][x]
        else:
            return -1
    return count
        
def six(y, x): 
    q = [[y, x], [y, x + 1], [y, x + 2]]

    count = 0

    for y,x in q:
        if 0 <= y < N and 0 <= x < M:
            count += maps[y][x]
        else:
            return -1
    return count
result = -1

for i in range(N):
    for j in range(M):
        result = max(result, one(i, j))
        result = max(result, two(i, j))
        result = max(result, three(i, j))
        result = max(result, four(i, j))
        result = max(result, five(i, j))
        result = max(result, six(i, j))

print(result)