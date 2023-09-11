#34184KB/	1200ms
import sys
from collections import deque
input = sys.stdin.readline
def bfs(l,x,y,mx,my):
    dx=[2,1,-1,-2,-2,-1,1,2]
    dy=[1,2,2,1,-1,-2,-2,-1]
    visited=[[False for _ in range(l+1)] for _ in range(l+1)]
    visited[x][y]=True
    queue=deque()
    queue.append((0,x,y)) # count, 현재 x, 현재 y
    while queue:
        count,nx,ny = queue.popleft()
        if nx==mx and ny==my: return count
        for i in range(8):
            nnx,nny = nx+dx[i],ny+dy[i]
            if 0<=nnx<l and 0<=nny<l and not visited[nnx][nny]:
                visited[nnx][nny] = True
                queue.append((count+1,nnx,nny))
    return 0
for _ in range(int(input())):
    l=int(input())
    nowX,nowY = map(int,input().split())
    moveX,moveY = map(int,input().split())
    print(bfs(l,nowX,nowY,moveX,moveY))
