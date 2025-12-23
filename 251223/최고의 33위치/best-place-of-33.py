N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
max_coin = -1

def coin_count(y, x):
    result = 0

    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if maps[i][j]:
                result += 1
    
    return result

for y in range(0, N - 2):
    for x in range(0, N - 2):
        max_coin = max(max_coin, coin_count(y, x))

print(max_coin)