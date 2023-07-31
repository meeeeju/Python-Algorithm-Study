# 64392KB / 1136ms (Python3)
# 131256 / 404ms (PyPy3)
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())

# 1
distTo1 = [float('inf')]*(N+1)
pq = [(0, 1)]
distTo1[1] = 0
while pq:
    distance, vertex = heappop(pq)
    for v in graph[vertex]:
        if distTo1[v[1]] > distance+v[0]:
            distTo1[v[1]] = distance+v[0]
            heappush(pq, (distance+v[0], v[1]))

# v1
distToV1 = [float('inf')]*(N+1)
pq = [(0, v1)]
distToV1[v1] = 0
while pq:
    distance, vertex = heappop(pq)
    for v in graph[vertex]:
        if distToV1[v[1]] > distance+v[0]:
            distToV1[v[1]] = distance+v[0]
            heappush(pq, (distance+v[0], v[1]))

# v2
distToV2 = [float('inf')]*(N+1)
pq = [(0, v2)]
distToV2[v2] = 0
while pq:
    distance, vertex = heappop(pq)
    for v in graph[vertex]:
        if distToV2[v[1]] > distance+v[0]:
            distToV2[v[1]] = distance+v[0]
            heappush(pq, (distance+v[0], v[1]))

ans = float('inf')
ansFlag = False
# 1->V1->V2->N or 1->V2->V1->N
if distTo1[v1]!=float('inf') and distToV1[v2]!=float('inf') and distToV2[N]!=float('inf'):
    ans = min(ans, distTo1[v1]+distToV1[v2]+distToV2[N])
    ansFlag = True
if distTo1[v2]!=float('inf') and distToV2[v1]!=float('inf') and distToV1[N]!=float('inf'):
    ans = min(ans, distTo1[v2]+distToV2[v1]+distToV1[N])
    ansFlag = True

if ansFlag:
    print(ans)
else:
    print(-1)