#왜 안되는지 모르겠음 ㅜ
n=int(input())

count=0
def dfs(node):
    global count
    count+=1
    visited[node]=(-1)**count
    for i in graph[node]:
        if visited[i]==0:
            count+=1
            visited[i]=(-1)**count
            dfs(i)
        

for _ in range(n):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited=[0]*(v+1)
    for _ in range(e):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
        for i in range(1,v+1):
            if visited[i]==0:
                dfs(i)
    
