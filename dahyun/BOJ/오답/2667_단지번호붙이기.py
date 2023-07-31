# 31332 KB / 40 ms
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def dfs(x,y):
    global cnt
    visited[x][y]=True
    cnt+=1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny]=='1' and not visited[nx][ny]: dfs(nx,ny)
    
N=int(input())
graph=[input().strip() for _ in range(N)] 
visited=[[False for _ in range(N)] for _ in range(N)] # 방문 여부 확인
dx=[0,0,1,-1]
dy = [1,-1,0,0]
result=[]  # 결과값
for i in range(N):
    for j in range(N):
        cnt=0 # 단지 수
        if graph[i][j]=='1' and not visited[i][j]: # 집이 있는 곳, 방문하지 않았을 경우 dfs 돌림
            dfs(i,j)
            result.append(cnt) # 단지 안에 있는 집 개수를 result에 추가
print(len(result))
for r in sorted(result): print(r)
