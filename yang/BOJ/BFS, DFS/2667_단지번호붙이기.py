# 34192KB / 64ms

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    visited[i][j] = True
    count = 0
    dq = deque()
    dq.append((i, j))
    while dq:
        i, j = dq.popleft()
        count += 1
        for k in range(4):
            x = i+dx[k]
            y = j+dy[k]
            if 0<=x<N and 0<=y<N:
                if not visited[x][y] and aparts[x][y]=='1':
                    visited[x][y] = True
                    dq.append((x, y))
    return count

N = int(input())
aparts = []
for _ in range(N):
    aparts.append(input().rstrip())
visited = [[False]*N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count_home = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and aparts[i][j]=='1':
            count = bfs(i, j)
            if count > 0:
                count_home.append(count)
count_home.sort()
print(len(count_home))
print(*count_home)