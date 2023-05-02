#31268 KB / 52 ms
import sys
input=sys.stdin.readline
def dfs(x,y,winner):
    global count
    visited[x][y]=True
    count+=1   # 같은 팀 병사 수 증가
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and war[nx][ny]==winner: # 이동한 위치가 범위 안에 있고, 방문한 적 없고, 같은 팀의 병사일 경우
            dfs(nx,ny,winner)
N,M = map(int,input().split())
war = []
visited=[[False for _ in range(N)] for _ in range(M)]
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1] 
for _ in range(M):
    war.append(list(map(str,input().strip())))
win,lose = 0,0
for i in range(M):
    for j in range(N):
        count=0
        if not visited[i][j]:
            dfs(i,j,war[i][j])
            if war[i][j]=='W': win+=(count**2)  # W면 우리팀 수(win)에 count의 제곱만큼 더해준다
            else: lose += (count**2)  # B면 상대팀 수(lose)에 count의 제곱만큼 더해준다
print(win,lose)
