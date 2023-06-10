# 다익스트라로 풀면 시간 초과남 
import sys
import heapq
input = sys.stdin.readline


INF = float('inf')

'''
input
4
5 2 4 3
6 5 1 2
3 4 5 3
7 4 3 1

output 
배열 탈출하기 위한 최소 비용
'''

N = int(input())
graph = [0 for _ in range(N+1)]

graph[0]=[0] * (N+1)
for i in range(1,N+1):
    graph[i]= [0]+ list(map(int,input().split()))


def dikstra(sx,sy):
    q=[]
    disTo = [[INF] * (N+1) for _ in range(N+1)]
    disTo[1][1]=0
    heapq.heappush(q,(0,sx,sy))

    dx = [0,1]
    dy =[1,0]

    while q:
        dis,x,y = heapq.heappop(q)

        if dis > disTo[x][y] :
            continue

        for i in range(2): 
            cost = 0
            nx = x+dx[i]
            ny = y+dy[i]
            if  nx > N  or ny >N:   # nx <= 0 or ny <=0 or
                continue
            if graph[nx][ny] >= graph[x][y]:
                cost = graph[nx][ny]-graph[x][y]+1
            if disTo[nx][ny] > disTo[x][y] + cost:
                disTo[nx][ny]= disTo[x][y] + cost
                if nx == N and ny == N :
                    return disTo[nx][ny]
                heapq.heappush(q,(disTo[nx][ny],nx,ny))    
    return -1

print(dikstra(1,1))




# heapq 에 튜플을 넣을시, 첫번째 값 기준으로 작동함