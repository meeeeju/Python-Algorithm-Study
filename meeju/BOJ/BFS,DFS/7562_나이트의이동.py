import sys
input = sys.stdin.readline
from queue import Queue
'''
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1'''

dx = [-2,-1,1,2,-2,-1,1,2] # j 열
dy = [-1,-2,-2,-1,1,2,2,1] # i 행

T = int(input())

N = int(input())
init = tuple(map(int,input().split()))
dest = tuple(map(int,input().split()))
visit=[[0 for _ in range(N)]for _ in range(N)]

def bfs():

    q = Queue()
    q.put((init[0],init[1],0))
    # visit[init[0]][init[1]] = 0

    while q:

        y,x,dis = q.get()
        if dis > visit[y][x]:
            continue
        
        if y == dest[0] and x == dest[1]:
            print(visit[dest[0]][dest[1]])
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visit[ny][nx] > dis+1:
                visit[ny][nx] = dis+1
                q.put(ny,nx,dis+1)
    
    return 

bfs()  

                    

