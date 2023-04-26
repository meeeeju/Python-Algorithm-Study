# 31268KB / 52ms
import sys
input = sys.stdin.readline

def dfs(start):
    if visited[start]: return
    visited[start] = True
    for s in graph[start]:
        if not visited[s]:
            dfs(s)

N = int(input())
M = int(input())
graph = [set() for _ in range(N+1)]
for i in range(1, N+1):
    line = list(map(int, input().split()))
    for r in range(N):
        if line[r] == 1:
            graph[i].add(r+1)
            graph[r+1].add(i)
plan = list(map(int, input().split()))

visited = [False]*(N+1)

dfs(plan[0])

for p in plan:
    if not visited[p]:
        print("NO")
        break
else:
    print("YES")
