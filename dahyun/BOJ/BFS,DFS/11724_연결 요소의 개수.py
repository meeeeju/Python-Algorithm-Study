# 65164 KB / 716 ms
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(v):
    for g in Graph[v]:
        if not visited[g]:
            visited[g]=True
            dfs(g)
N,M = map(int,input().split())
Graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
visited[0]=True
for _ in range(M):
    u,v = map(int,input().split())
    Graph[u].append(v)
    Graph[v].append(u)
result=0
for i in range(1,N+1):
    if not visited[i]: # 방문하지 않은 정점만 시작점으로 정함 (모든 정점에 대해 연결점이 있는지 확인 !)
        dfs(i)
        result+=1
print(result)

