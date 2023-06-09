#시간초과 계속 나 ㅠ
import sys
import heapq
# from collections import deque
input = sys.stdin.readline
def bfs():
    queue=[(0,0,0)]
    # queue=deque()
    # queue.append((0,0,0))
    # money[0][0]=nlist[0][0]
    while queue:
        m,x,y = heapq.heappop(queue)
        # m,x,y = queue.pop(0)
        # m,x,y = queue.popleft()
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if nx==n-1 and ny==n-1 : return
                if nlist[x][y]>nlist[nx][ny] and money[nx][ny]>m:
                    money[nx][ny]=m
                    # if nx==n-1 and ny==n-1 : return
                    heapq.heappush(queue,(money[nx][ny],nx,ny))
                    # queue.append((money[nx][ny],nx,ny))
                elif nlist[x][y]<=nlist[nx][ny] and money[nx][ny]>(nlist[nx][ny]-nlist[x][y])+1+m:
                    money[nx][ny] = (nlist[nx][ny]-nlist[x][y])+1+m
                    # if nx==n-1 and ny==n-1 : return 
                    heapq.heappush(queue,(money[nx][ny],nx,ny))
                    # queue.append((money[nx][ny],nx,ny))
                    

n= int(input())
nlist = [list(map(int,input().split())) for _ in range(n)]
money=[[1000000000 for _ in range(n)] for _ in range(n)]
d = [(0,1),(1,0)]
bfs()
print(money[n-1][n-1])
