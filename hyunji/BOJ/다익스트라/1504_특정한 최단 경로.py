#solution 1, solution 2 방법 블로그 참고! 신기방기

#메모리 :64260 #시간 :560
import heapq
import sys
input=sys.stdin.readline

def dijkstra(start,end):
    visited=[1e8]*(n+1)
    heap=[]
    heapq.heappush(heap,(0,start))
    visited[start]=0

    while heap:
        cost,node=heapq.heappop(heap)
        if visited[node]<cost:
            continue

        for i in graph[node]:
            nextcost,nextnode=i
            if visited[nextnode]>nextcost+cost:
                visited[nextnode]=nextcost+cost
                heapq.heappush(heap,(nextcost+cost,nextnode))
    return visited[end]

n,e=map(int,input().split())
graph=[[] for _ in range(n+1)]
#visited=[1e8]*(n+1)
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1,v2=map(int,input().split())

solution1=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
solution2=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)

if solution1>=1e8 and solution2>=1e8:
    print(-1)
else:
    print(min(solution1,solution2))
