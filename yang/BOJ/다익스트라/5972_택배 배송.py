# 51560KB / 236ms
import sys
from heapq import heappop, heappush
sysInput = sys.stdin.readline
N, M = map(int, sysInput().split())
distance = [-1]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sysInput().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
pq = [(0, 1)] # 거리, 정점
while pq:
    d, v = heappop(pq)
    if distance[v] > -1: continue
    distance[v] = d
    if v == N : break
    for g in graph[v]:
        if distance[g[1]] == -1:
            heappush(pq, (d+g[0], g[1]))
print(distance[N])