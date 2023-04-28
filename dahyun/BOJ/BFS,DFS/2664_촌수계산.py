#BaekJoon 2664 촌수계산
# 31256 KB / 40 ms
import sys
input=sys.stdin.readline

def dfs(n,cnt):
    visited[n]=cnt  # 촌수 저장
    for g in graph[n]:
        if visited[g]==-1:
            dfs(g,cnt+1)
            
n=int(input())
p,q=map(int,input().split())
graph=[-1]+[[] for _ in range(n)]
visited=[-1 for _ in range(n+1)]
for _ in range(int(input())):
    x,y = map(int,input().split()) # x : 부모  , y : 자식
    graph[y].append(x)  # 촌수는 위로도, 아래로도 계산할 수 있으므로 양방향으로 연결해준다
    graph[x].append(y)
    
dfs(p,0)  

if visited[q]==-1 or visited[p]==-1 : print(-1)  # q를 한 번도 방문하지 않거나, p를 한 번도 방문하지 않거나 -> 둘은 친척 x
else: print(visited[q])
