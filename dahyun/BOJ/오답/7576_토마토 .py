#146760KB/	1168ms
import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    global total
    to = deque()
    for i,j in tomato:
        to.append((1,i,j))
    while to:
        n,x,y = to.popleft()
        for dirx,diry in dir:
            nx,ny = x+dirx,y+diry
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                graph[nx][ny]=1
                total-=1
                if total==0: return n
                to.append((n+1,nx,ny))
    return -1
                
dir = [(1,0),(-1,0),(0,1),(0,-1)]
M,N = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
total = 0 ; tomato=[] ; result=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==0: total+=1
        elif graph[i][j]==1: tomato.append((i,j))
if total==0 and tomato: print(0)
else: 
    result=bfs()
    if result>-1: print(result)
    else: print(-1)
