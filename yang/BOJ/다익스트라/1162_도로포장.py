# 블로그 참고
from sys import stdin
from heapq import heappop, heappush
sinput = stdin.readline

N, M, K = map(int, sinput().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sinput().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance_with_count = [[float('inf')]*(K+1) for _ in range(N+1)] # dp[i][j] : 정점 i 에서 j 만큼 포장했을때의 거리
hp = []
heappush(hp, (0, 1, 0)) # 거리, 정점, 포장횟수
# for i in range(K+1):
#     distance_with_count[1][i] = 0
while hp:
    distance, vertex, count = heappop(hp)
    if vertex==N:
        print(distance)
        break
    if distance_with_count[vertex][count] < distance:
        continue
    for next_vertext, next_distance in graph[vertex]:
        if count < K and distance < distance_with_count[next_vertext][count+1]:
            distance_with_count[next_vertext][count+1] = distance
            heappush(hp, (distance_with_count[next_vertext][count+1], next_vertext, count+1))
        if distance+next_distance < distance_with_count[next_vertext][count]:
            distance_with_count[next_vertext][count] = distance+next_distance
            heappush(hp, (distance_with_count[next_vertext][count], next_vertext, count))
# print(min(distance_with_count[N]))