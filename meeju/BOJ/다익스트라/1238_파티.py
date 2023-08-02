# 	34348	956
import sys
import heapq
input = sys.stdin.readline

'''
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3'''


N, M, x = map(int,input().split()) # N 명, M 개, x 번

villege = [[] for _ in range(N+1)]

for i in range(M):
    v,w,dis = map(int,input().split())
    villege[v].append((w,dis))

def dikstra(s,e):

    visited = [False for _ in range(N+1)]
    dis =[float('inf') for _ in range(N+1)]

    q=[(0,s)]
    visited[s] = True
    dis[s]= 0 

    while q :
        cost, v = heapq.heappop(q)

        if v == e :
            return cost
        if cost > dis[v]:
            continue
        for w,w_cost in villege[v]:

            if dis[w] > dis[v]+ w_cost :
                dis[w] = dis[v]+w_cost
                heapq.heappush(q,(dis[w],w))
result = []
for i in range(1,N+1):

    shortest_dis = dikstra(i,x)
    shortest_dis +=dikstra(x,i)
    result.append(shortest_dis)

    
# print(result)
print(max(result))

