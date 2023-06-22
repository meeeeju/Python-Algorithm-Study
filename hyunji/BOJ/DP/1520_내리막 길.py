import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

m,n=map(int,input().split())
liist=[]
for _ in range(m):
    liist.append(list(map(int,input().split())))

dp=[[-1]*n for _ in range(m)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    
    ways=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and liist[x][y]>liist[nx][ny]:
            ways+=dfs(nx,ny)
    
    return ways


print(dfs(0,0))
