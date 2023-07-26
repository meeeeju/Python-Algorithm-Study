import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int,input().split())
box = []
queue = deque([])
 
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(M):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    box.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue): # bfs
    x,y,z = queue.popleft()
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<H and 0<=b<N and 0<=c<M and box[a][b][c]==0:
            queue.append([a,b,c])
            box[a][b][c] = box[x][y][z]+1
            
day = 0
for i in box:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)