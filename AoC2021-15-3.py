from sortedcontainers import SortedList

data = open("AoC2021-15.input").read()

data = [list(map(int,d.strip())) for d in data.strip().splitlines()]

INF = float('inf')

W = len(data[0])
H = len(data)

newdata = [[0] * (W*5) for _ in range(H*5)]

for y in range(5):
    for x in range(5):
        for yy in range(H):
            for xx in range(W):
                newdata[yy + y * H][xx + x * W] = (data[yy][xx] + y + x - 1) % 9 + 1

data = newdata

W = len(data[0])
H = len(data)

walk = [[INF] * (W) for _ in range(H)]
walk[0][0] = 0

visited = {(0, 0)}

def step(data, walk, visited):
    if not visited:
        return False
    xx, yy = min(visited, key=lambda x:walk[x[1]][x[0]] if walk[x[1]][x[0]] > 0 else INF )
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        x = xx + dx
        y = yy + dy
        if (0<=x<W) and (0<=y<H):
            if walk[y][x] <= 0:
                continue
            np = data[y][x] + walk[yy][xx]
            if walk[y][x] > np:
                visited.add((x, y))
                walk[y][x] = np
    walk[yy][xx] = -walk[yy][xx]
    visited.remove((xx,yy))
    return True


s = 0
while step(data, walk, visited):
    s += 1
    if s % W == 0:
        print(f"\r{s:8} of {W * H:8}", end='')

print()
print(-walk[H-1][W-1])
