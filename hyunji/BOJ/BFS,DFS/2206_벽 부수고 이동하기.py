#블로그참고
from collections import deque
n,m=map(int,input().split())
liist=[]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
visited=[[[0]*2 for _ in range(m)]for _ in range(n)]
visited[0][0][0]=1
for _ in range(n):
    string=list(map(int,input()))
    liist.append(string)

def bfs(a,b,c):
    queue=deque()
    queue.append((a,b,c))
    while queue:
        x,y,z=queue.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][z]
        for i in range(4):
            nextX=x+dx[i]
            nextY=y+dy[i]

            if 0<=nextX<n and 0<=nextY<m:
                if liist[nextX][nextY]==0 and visited[nextX][nextY][z]==0:
                    visited[nextX][nextY][z]=visited[x][y][z]+1
                    queue.append((nextX,nextY,z))
                elif liist[nextX][nextY]==1 and z==0:
                    visited[nextX][nextY][1]=visited[x][y][0]+1
                    queue.append((nextX,nextY,1))
    return -1
                
print(bfs(0,0,0))
