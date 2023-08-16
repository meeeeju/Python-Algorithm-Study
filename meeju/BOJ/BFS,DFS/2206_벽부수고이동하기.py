# bfs 시간 초과 -> 블로그 https://kscodebase.tistory.com/66
import sys
from collections import deque
input = sys.stdin.readline

# 14502 연구소랑 비슷 

'''
6 4
0100
1110
1000
0000
0111
0000'''

N, M = map(int,input().split()) # N : 행
maps = [0 for _ in range(N)]

for i in range(N):
    raw = list(map(int,input().rstrip()))
    maps[i] = raw

di = [0,0,1,-1]
dj = [-1,1,0,0]

def bfs():
    copy_maps = [[maps[i][j] for j in range(M)] for i in range(N)]
    q = deque()
    q.append((0,0,1))
    
    copy_maps[0][0]= 1 # 1이면 방문처리

    while q:
    
        x,y,cnt = q.popleft()
        for k in range(4):
            nx = x+ di[k]
            ny = y + dj[k]
            if (nx,ny) == (N-1,M-1):
                return cnt+1
            if nx < 0 or nx >= N :  # 범위에 벗어나면 Pass
                continue
            if ny < 0 or ny >= M :
                continue
            if copy_maps[nx][ny]:   # 이미 방문한 지점이라면 Pass
                continue
            
            copy_maps[nx][ny]=1
            q.append((nx,ny,cnt+1))
        
    return float('inf')

result = bfs()
            
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1 :    # 벽이라면
            maps[i][j] = 0
            cnt = bfs()
            result= min(cnt,result)
            maps[i][j] = 1

if result == float('inf'):
    print(-1)
else:
    print(result)


            

        



