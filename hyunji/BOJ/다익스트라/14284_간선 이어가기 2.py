#메모리 :52780 시간 :276
import heapq
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]


def dijkstra(s,t):
    visited=[1e8]*(n+1)
    heap=[]
    heapq.heappush(heap,(0,s))
    visited[s]=0

    while heap:
        cost,node=heapq.heappop(heap)
        if visited[node]<cost:
            continue

        for i in graph[node]:
            nextcost,nextnode=i
            if visited[nextnode]>cost+nextcost:
                visited[nextnode]=cost+nextcost
                heapq.heappush(heap,(nextcost+cost,nextnode))
    return visited[t]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

s,t=map(int,input().split())

print(dijkstra(s,t))
