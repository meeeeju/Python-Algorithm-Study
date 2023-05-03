#블로그 참고
#메모리 :79316 시간 :572
import sys
input=sys.stdin.readline
from collections import deque

F,S,G,U,D=map(int,input().split())
visited=[0]*(F+1)
graph=[0 for _ in range(F+1)]

def dfs(node):
    q=deque([node])
    visited[node]=1
    while q:
        node=q.popleft()
        
        if node==G:
            return graph[G]
        
        for i in (node+U,node-D):
            if 0<i<=F and not visited[i]:
                visited[i]=1
                graph[i]=graph[node]+1
                q.append(i)

    if graph[G]==0:
            return "use the stairs"

print(dfs(S))


