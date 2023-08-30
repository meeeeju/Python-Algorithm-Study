# 52780KB / 228ms
from sys import stdin
from heapq import heappop, heappush
sinput = stdin.readline

N, M = map(int, sinput().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sinput().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
S, T = map(int, sinput().split())
distance_from_S = [float('inf')]*(N+1)
hp = []
heappush(hp, (0, S))
distance_from_S[S] = 0
while hp:
    distance, vertex = heappop(hp)
    if vertex==T:
        print(distance)
        break
    for next_vertex, move_distance in graph[vertex]:
        if distance_from_S[next_vertex] > distance_from_S[vertex]+move_distance:
            distance_from_S[next_vertex] = distance_from_S[vertex]+move_distance
            heappush(hp, (distance_from_S[next_vertex], next_vertex))