# dfs로 풀었음 ,, 다익스트라로 이거 풀 수 있나?!
# 31332 KB / 40 ms
import sys
input = sys.stdin.readline
def dfs(x,y):
    global count
    visited[x][y]=True
    count+=1
    for i in range(4):  # 상하좌우
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and nlist[nx][ny]=='1':  # nx,ny가 범위에 존재, 방문하지 않았을 때, 지도상 집이 있을 때
            dfs(nx,ny)
    
N=int(input())
nlist = [list(map(str,input().strip())) for _ in range(N)]  # 지도
visited=[[False for _ in range(N)] for _ in range(N)]  # 방문 여부
dx=[1,-1,0,0]  
dy=[0,0,1,-1]
result=[]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and nlist[i][j]=='1':  # 방문하지 않고, 집이 존재할 때
            count=0  # 집의 개수
            dfs(i,j)
            result.append(count)
result.sort()  # 오름차순 정렬
print(len(result))
for r in result: print(r)
