# 34112	68
import sys
from collections import deque
input = sys.stdin.readline

'''
6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0'''

N,M,T = map(int,input().split())
castle_map = [0 for _ in range(N)]
# visited = [0 for _ in range()]

for i in range(N):
    castle = list(map(int,input().split()))
    castle_map[i]=castle


dx = [0,0,-1,1]
dy =[-1,1,0,0]

def bfs():

    d = deque()
    d.append((0,0,0)) # x,y,t
    answer =[]

    while d:

        x,y,t = d.popleft()

        if t >= T : # 제한 시간을 초과하면 
            continue

        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 갈수있는 방향 조건 체크
                continue
            if castle_map[nx][ny] == 1: # 벽을 만나면 pass and 방문 처리
                continue
            if castle_map[nx][ny] == 2:
                temp = N-1- nx + M-1-ny + 1 + t
                if temp <= T:
                    answer.append(temp)
                castle_map[nx][ny] == 1

            elif nx == (N-1) and ny == (M-1):
                answer.append(t+1)
                return answer
            else:
                castle_map[nx][ny]=1
                d.append((nx,ny,t+1))
    return answer
result = bfs()   
if result:
    print(min(result))
else:
    print("Fail")

