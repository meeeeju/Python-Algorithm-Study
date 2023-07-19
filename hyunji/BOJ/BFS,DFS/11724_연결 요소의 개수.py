#recursion error나서 setrecursionlimit 설정해주는거 블로그 찾아봄!
#메모리 :65129 시간 :700
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
count=0

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node]=True
    for i in graph[node]:
        if not visited[i]:
            visited[i]=True
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        visited[i]=True
        dfs(i)
        count+=1
print(count)
