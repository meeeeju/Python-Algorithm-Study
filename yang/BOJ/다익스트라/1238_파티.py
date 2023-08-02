# 72256KB / 2080ms
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
MAX_DISTANCE = 100*10000+1
N, M, X = map(int, input().split())
X = X-1
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a-1].append((t, b-1))

distance = [[MAX_DISTANCE]*(N) for _ in range(N)]
for i in range(N): # 0~N-1 각각 다익스트라
    distance[i][i] = 0
    pq = []
    for a in graph[i]:
        heappush(pq, a) # a는 (t, b) 튜플
        distance[i][a[1]] = a[0]
    while pq:
        t, b = heappop(pq)
        for v in graph[b]:
            if distance[i][v[1]] > v[0]+t:
                heappush(pq, (v[0]+t, v[1]))
                distance[i][v[1]] = v[0]+t
ansDistance = 0
for i in range(N):
    ansDistance = max(ansDistance, distance[i][X]+distance[X][i])
print(ansDistance)