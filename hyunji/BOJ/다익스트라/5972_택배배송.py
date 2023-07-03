#메모리 :51560 시간 :240
import heapq
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[1e8]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(node):
    heap=[]
    heapq.heappush(heap,(0,node))
    visited[node]=0

    while heap:
        cost,node=heapq.heappop(heap)
        if visited[node]<cost:
            continue

        for i in graph[node]:
            nextnode,nextcost=i
            if visited[nextnode]>nextcost+cost:
                visited[nextnode]=nextcost+cost
                heapq.heappush(heap,(nextcost+cost,nextnode))

dijkstra(1)
print(visited[n])
