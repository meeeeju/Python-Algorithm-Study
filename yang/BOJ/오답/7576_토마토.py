# 98640KB / 2512ms (Python3)
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
storage = []
dq = deque()
for i in range(N):
    storage.append(list(map(int, input().split())))
    for j in range(M):
        if storage[i][j]==1: # 익은 토마토 위치
            dq.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0
while dq:
    x, y = dq.popleft()
    for v in range(4):
        nextX = x+dx[v]
        nextY = y+dy[v]
        if 0<=nextX<N and 0<=nextY<M:
            if storage[nextX][nextY] == 0: # 안익은 토마토
                storage[nextX][nextY] = storage[x][y] + 1
                dq.append((nextX, nextY))

# 정답 구하기
day = 0
is_all_cooked = True
for i in range(N):
    for j in range(M):
        if storage[i][j] == 0:
            is_all_cooked = False
        day = max(day, storage[i][j])

if is_all_cooked: print(day-1)
else: print(-1)
