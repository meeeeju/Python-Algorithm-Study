#52780KB/ 292ms
import sys
import heapq
input = sys.stdin.readline
def dijkstra(start):
    queue=[(0,start)]  # 가중치, 시작점
    distance=[10000000 for _ in range(n+1)]  # 거리 초기화
    distance[start]=0  # 시작점은 0
    while queue:
        w,s = heapq.heappop(queue)  # 가중치, 시작점
        for (b,c) in graph[s]:  # b: 도착지, c : s<->b의 가중치
            if distance[b]>distance[s]+c:  # 만약, distance[도착지]가 (distance[시작점]+ s<->b의 가중치)보다 크다면
                distance[b]=distance[s]+c  # 초기화
                heapq.heappush(queue,(distance[b],b)) # 모든 그래프는 연결되어 있으므로, 초기화될 때만 heapq에 넣어줌
    return distance
    
n,m = map(int,input().split())  # n : 정점 , m : 간선
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,c =  map(int,input().split())  
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t = map(int,input().split())

print(dijkstra(s)[t])
