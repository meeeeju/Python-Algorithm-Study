# 51572KB / 1368ms
import sys
from collections import deque

def isBipartite(start):
    dq = deque()
    dq.append(start)
    color[start] = 0
    while dq:
        v = dq.popleft()
        for u in graph[v]:
            if color[u] == -1:
                color[u] = 1 if color[v]==0 else 0
                dq.append(u)
            elif color[u] == color[v]:
                return False
    return True

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    color = [-1]*V # 초기값 -1, 빨간색 0, 파란색 1
    for i in range(V):
        if color[i] == -1:
            if not isBipartite(i):
                print("NO")
                break
    else:
        print("YES")