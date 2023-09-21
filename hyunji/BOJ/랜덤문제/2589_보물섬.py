from collections import deque
a,b=map(int,input().split())

def bfs(i,j):
    queue=deque()
    visited=[[0]*b for _ in range(a)]
    queue.append((i,j))
    visited[i][j]=1
    count=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y

            if nx>=a or nx<0 or ny>=b or ny<0:
                continue
            elif map[nx][ny]=='L' and visited[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                count=max(visited[nx][ny],count)
                queue.append((nx,ny))
    return count-1

dx=[1,-1,0,0]
dy=[0,0,1,-1]
map=[]
for _ in range(a):
    map.append(list(input()))
maxx=0
for i in range(a):
    for j in range(b):
        if map[i][j]=='L':
            maxx=max(maxx,bfs(i,j))
print(maxx)
