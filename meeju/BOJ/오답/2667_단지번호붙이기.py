# 31348	48

import sys
input = sys.stdin.readline

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000'''

N  = int(input())
maps = [0 for _ in range(N)]

for i in range(N):
    raw = list(map(int,input().rstrip()))
    maps[i] = raw


def dfs(x,y):
    global cnt
    maps[x][y]=0
    cnt +=1

    dx =[-1,0,1,0]
    dy =[0,-1,0,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if maps[nx][ny] ==0:
            continue
        dfs(nx,ny)


cnt = 0 
result =[]
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            cnt = 0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()

for i in result:
    print(i)