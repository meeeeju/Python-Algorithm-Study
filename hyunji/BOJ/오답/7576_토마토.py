#0<=nextX<n and 0<=nextY<m 이부분이 이해가 안돼서 블로그 찾아봄!
import sys
input=sys.stdin.readline

from collections import deque
m,n=map(int,input().split())
box=[]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
queue=deque([])
for _ in range(n):
    box.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            queue.append([i,j])

def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nextX=x+dx[i]
            nextY=y+dy[i]

            if 0<=nextX<n and 0<=nextY<m and box[nextX][nextY]==0:
                box[nextX][nextY]=box[x][y]+1
                queue.append([nextX,nextY])

bfs()
maxx=0
for i in range(n):
    for j in range(m):
        if box[i][j]==0:
            print(-1)
            break
        maxx=max(maxx,box[i][j])
print(maxx-1)
