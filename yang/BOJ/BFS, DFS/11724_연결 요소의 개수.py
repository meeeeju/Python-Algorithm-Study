# 65104KB / 756ms
import sys
input = sys.stdin.readline

def dfs(i):
    visited[i] = True
    stack = [i]
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
visited = [False] * N
ans = 0
for i in range(N):
    if not visited[i]:
        ans += 1
        dfs(i)
print(ans)