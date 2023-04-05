# 31256KB / 156ms
import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(tuple(map(int, input().split())))

ans = [[0]*(N) for _ in range(N)]
for i in range(N):
    q = []
    for k in range(N):
        if graph[i][k] == 1:
            q.append(k)
            ans[i][k] = 1
    while q:
        s = q.pop(0)
        for k in range(N):
            if graph[s][k] == 1 and ans[i][k] == 0:
                ans[i][k] = 1
                q.append(k)
for a in ans:
    print(*a)