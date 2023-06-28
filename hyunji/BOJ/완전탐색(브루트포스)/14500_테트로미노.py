#블로그 코드,, 문제가 이해가 안됨 ㅠ
n,m=map(int,input().split())
liist=[]
visited=[[0]*m for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,1,0,-1]
ans=0
maxx=max(map(max,liist))

def dfs(r,c,idx,total):
    global ans
    if ans>=total+maxx*(3-idx):
        return
    if idx==3:
        ans=max(ans,total)
        return
    else:
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if 0<=nr<n and 0<=nc<m and visited[nr][nc]==0:
                if idx==1:
                    visited[nr][nc]=1
                    dfs(r,c,idx+1,total+liist[nr][nc])
                    visited[nr][nc]=0
                visited[nr][nc]=0
                dfs(r,c,idx+1,total+liist[nr][nc])
                visited[nr][nc]=0


for _ in range(n):
    a=list(map(int,input().split()))
    liist.append(a)

for r in range(n):
    for c in range(m):
        visited[r][c]=1
        dfs(r,c,0,liist[r][c])
        visited[r][c]=0

print(ans)
