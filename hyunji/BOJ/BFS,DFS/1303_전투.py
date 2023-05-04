#블로그 참고
#메모리 :34160 시간 :80
from collections import deque
n,m=map(int,input().split())
graph=[list(input()) for _ in range(m)]
visited=[[0]*n for _ in range(m)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y,color):
    count=0
    q=deque()
    q.append((x,y))
    visited[x][y]=1

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==color and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    count+=1

    return count+1

white,blue=0,0
for i in range(m):
    for j in range(n):
        if graph[i][j]=='W' and visited[i][j]==0:
            white+=bfs(i,j,'W')**2
        elif graph[i][j]=='B' and visited[i][j]==0:
            blue+=bfs(i,j,'B')**2

print(white,blue)
