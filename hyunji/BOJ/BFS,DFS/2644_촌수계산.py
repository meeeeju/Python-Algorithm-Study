#메모리 :31256 시간 :40
import sys
input=sys.stdin.readline

n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)

def dfs(node):
    for i in graph[node]:
        if visited[i]==0:
            visited[i]=visited[node]+1
            dfs(i)

for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a)
if visited[b]>0:
    print(visited[b])
else:
    print(-1)
