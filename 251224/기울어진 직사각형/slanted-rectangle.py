import copy

N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]

result = -1
move = [[-1,1], [-1,-1], [1, -1], [1,1]]

def is_coordinate(y, x):
    if 0 > y or N <= y or 0 > x or N <= x:
        return False
    return True

def check_square(y, x, w, h):
    n = 0
    p = [w, h, w, h]

    for i in range(4):
        for _ in range(p[i]):
            y, x = y + move[i][0], x + move[i][1]
            
            if not is_coordinate(y, x):
                return 0

            n += maps[y][x]    

    return n

for y in range(N):
    for x in range(N):
        for w in range(1, N):
            for h in range(1, N):
                result = max(result, check_square(y, x, w, h))

print(result)