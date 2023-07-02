# 135272KB / 1332ms (Python3)
# 178804KB / 924ms (PyPy3)

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
goal = N-1
maxTime = 300000*10000+1
distance = [maxTime if not i else -1 for i in map(int, input().split())]
distance[goal] = maxTime
connected = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    connected[a].append((b, t))
    connected[b].append((a, t))

hq = []
heappush(hq, (0, 0)) # 거리, 위치
while hq:
    d, p = heappop(hq)
    if distance[p] != maxTime: continue
    distance[p] = d
    if p==goal: break
    for c, t in connected[p]:
        if distance[c] != -1 and distance[c] == maxTime:
            heappush(hq, (d+t, c))
print(-1 if distance[goal]==maxTime else distance[goal])