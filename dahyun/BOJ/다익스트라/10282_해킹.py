#BaekJoon 10282 해킹
# 블로그 참고해서 코드 수정함 ㅠㅜ
# 48684 KB /824 ms
import sys
import heapq
input=sys.stdin.readline
'''
def dijkstra(start):    # 48152 KB /1316 ms   -> 단순히 노드 수를 가지고 min heap 사용했을 때, 오래걸림
    queue=[start]
    distance=[100000000000 for _ in range(n+1)]  # 해당 노드까지의 최단 거리 저장하는 배열
    distance[start]=0  # 시작 노드는 최단 거리 0
    while queue:
        q=heapq.heappop(queue)  # 큐에 들어가 있는 값들 중에 제일 작은 값 pop
        for g,s in graph[q]:
            if distance[q]+s<distance[g]:
                distance[g]=distance[q]+s
                heapq.heappush(queue,g)
    return distance
'''
def dijkstra(start):
    queue=[(0,start)]
    distance=[100000000000 for _ in range(n+1)]  # 해당 노드까지의 최단 거리 저장하는 배열
    distance[start]=0  # 시작 노드는 최단 거리 0
    while queue:
        s,q=heapq.heappop(queue)  # 큐에 들어가 있는 값들 중에 제일 작은 값 pop
        for g,s in graph[q]:
            if distance[q]+s<distance[g]:  # 거리가 최단인 것을 구하면, queue에 넣어줌
                distance[g]=distance[q]+s
                heapq.heappush(queue,(distance[g],g))
    return distance

for _ in range(int(input())):
    n,d,c = map(int,input().split())
    graph=[[] for _ in range(n+1)]
    
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    
    distance=dijkstra(c)
    count,clock=0,-1
    for d in distance:
        if d!=100000000000:
            count+=1
            clock=max(clock,d)
    print(count,clock)

