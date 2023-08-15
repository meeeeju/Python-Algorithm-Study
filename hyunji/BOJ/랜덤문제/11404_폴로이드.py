#블로그 참고
#메모리 :33324 시간 :644
import sys
input=sys.stdin.readline
import heapq
n=int(input())
m=int(input())

graph=[[1e8]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(graph[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j]=0
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==1e8:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

'''
def dijkstra(a,b):
    visited=[1e8]*(n+1)
    heap=[]
    heapq.heappush(heap,(0,a))
    visited[a]=0

    while heap:
        cost,node=heapq.heappop(heap)
        if visited[node]<cost:
            continue

        for i in graph[node]:
            nextnode,nextcost=i
            if visited[nextnode]>nextcost+cost:
                visited[nextnode]=nextcost+cost
                heapq.heappush(heap,(nextcost+cost,nextnode))
    return visited[b]


for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

print(graph)   
result=[[1e8]*(n) for _ in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            result[i-1][j-1]=0
        else:
            result[i-1][j-1]=dijkstra(i,j)
    
for i in range(n):
    print(*result[i])'''
