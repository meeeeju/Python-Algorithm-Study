# 31256 KB / 64 ms
import sys
input = sys.stdin.readline
def bfs(sx,sy):
    global area 
    queue=[(sx,sy)]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<M and 0<=ny<N and not square[nx][ny]:
                square[nx][ny]=True
                area+=1
                queue.append((nx,ny))
        
M,N,K = map(int,input().split())
# 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
square = [[False for _ in range(N)] for _ in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(K):
    sx,sy,fx,fy = map(int,input().split())
    for x in range(sy,fy):
        for y in range(sx,fx):
            if 0<=x<M and 0<=y<N: square[x][y]=True
count=0
result=[]
for x in range(M):
    for y in range(N):
        if not square[x][y]:
            area = 1
            square[x][y]=True
            bfs(x,y)
            result.append(area)
            count+=1

print(count)
print(*sorted(result))
