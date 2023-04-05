# 98604KB / 1408ms
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
ans = []
visited = [False]*(N+1)
q = [(X, 0)]
visited[X] = True
while q:
    x, distance = q.pop(0)
    if distance == K:
        ans.append(x)
    elif distance > K:
        break
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            q.append((i, distance+1))
if ans:
    ans.sort()
    print(*ans)
else:
    print(-1)