#107104kb / 	2500ms
from queue import Queue
import sys
input = sys.stdin.readline

# 정점 간 거리가 모두 1로 같음 -> bfs or dfs
'''
4 4 2 1
1 2
1 3
2 3
2 4'''

N, M, K, X = map(int,input().split()) # N:도시 / M:도로 / K:거리 정보 / X:출발 도시


graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)

def bfs(s):

    visited = [False for _ in range(N+1)]
    distance = [0 for _ in range(N+1)]

    q = Queue()
    q.put(s)
    visited[s]=True
    
    while (q.qsize()>0) :
        v = q.get()
        for w in graph[v]:
            if not visited[w] : # 아직 방문하지 않았더라면
                visited[w] = True
                distance[w]= distance[v]+1
                q.put(w)
    
    return distance


shortedsDistance = bfs(X)
result = []


for i in range(1,N+1):
    if shortedsDistance[i] == K : 
        result.append(i)

result.sort()
if result:
    print(*result,sep='\n')
else:
    print(-1)


