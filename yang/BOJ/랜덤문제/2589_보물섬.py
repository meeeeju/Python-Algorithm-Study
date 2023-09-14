# 121076KB / 676ms (PyPy3)

from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    distance = [[-1]*W for _ in range(H)]

    dq = deque()
    dq.append((x, y))
    distance[x][y] = 0
    result = 0

    while dq:
        x, y = dq.popleft()
        for v in range(4):
            next_x = dx[v]+x
            next_y = dy[v]+y
            if 0<=next_x<H and 0<=next_y<W:
                if treasure_map[next_x][next_y]==l and distance[next_x][next_y]==-1:
                    distance[next_x][next_y] = distance[x][y]+1
                    result = max(result, distance[next_x][next_y])
                    dq.append((next_x, next_y))

    return result


H, W = map(int, input().split())
treasure_map = []
for _ in range(H):
    treasure_map.append(input().rstrip())

l = "L"
ans = 0
for i in range(H):
    for j in range(W):
        if treasure_map[i][j]==l:
            ans = max(ans, bfs(i, j))
print(ans)