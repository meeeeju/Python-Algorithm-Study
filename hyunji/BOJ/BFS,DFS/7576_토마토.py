#메모리 :10680 시간 :1460
from collections import deque
import sys
inpyt=sys.stdin.readline

m,n=map(int,input().split())
liist=[]
for _ in range(n):
    a=list(map(int,input().split()))
    liist.append(a)

queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if liist[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and liist[nx][ny] == 0:
                liist[nx][ny] = liist[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in liist:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)
