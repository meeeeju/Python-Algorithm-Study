# 244064 KB / 564 ms
import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    global total
    queue=deque()
    for x,y in start:  # 토마토가 열려있는 좌표들 모두 queue에 저장
        queue.append((1,x,y)) 
    while queue:
        day,x,y = queue.popleft() # 날짜, 좌표
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and nlist[nx][ny]==0:
                nlist[nx][ny]=1
                total-=1  # 토마토가 익음으로 인해 total 감소
                if total==0: return day  # 토마토가 다 익었으면 날짜 반
                queue.append((day+1,nx,ny))
    return -1
M,N = map(int,input().split())
start=[]; nlist=[] ; total=0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(M):
        if temp[j]==0: total+=1  # total : 토마토가 익지 않은 개수
        if temp[j]==1: start.append((i,j)) # start : 토마토가 익었는 위치
    nlist.append(temp) # nlist : 밭

if total==0 and start: print(0)  # 토마토가 익지 않은 개수가 0이고 익었는 개수가 존재한다.
else:
    result=bfs()
    if result > -1 : print(result);exit()
    print(-1)
