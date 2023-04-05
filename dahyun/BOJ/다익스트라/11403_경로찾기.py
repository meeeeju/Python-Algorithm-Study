# 31256 KB / 52 ms
import sys
def dfs(start):
    visited[start]=True
    for g in graph[start]:
        if g==i : result[i][i]=1  # 만약 자기 자신으로 돌아온다면, 경로가 있다고 표시
        if not visited[g]:
            result[i][g]=1  # 출발지 i 에서 g까지 온 것이므로 , result[i][g]를 1로 초기화해준다
            dfs(g)

N=int(sys.stdin.readline())  # 정점 개수
graph=[[] for _ in range(N)]  # 연결되어 있는 그래프 저장
G=[]  # 임시 그래프
result=[[0 for _ in range(N)] for _ in range(N)]   # 연결되어 있는지 저장하는 그래프
for i in range(N):
    G.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if G[i][j]==1: graph[i].append(j)
visited=[]
for i in range(N):
    visited.clear()
    visited=[False for _ in range(N)]
    dfs(i)
for i in range(N):
    print(*result[i])
