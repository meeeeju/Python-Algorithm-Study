#블로그 참고 알거같으면서도...좀 모르겠음..
#메모리 :315596 시간 :5548

import sys
input=sys.stdin.readline 
sys.setrecursionlimit(10**9)

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
dp=[[0,0] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node]=1
    dp[node][0]=0
    dp[node][1]=1

    for i in graph[node]:
        if visited[i]==0:
            visited[i]=1
            dfs(i)

            dp[node][0]+=dp[i][1]
            dp[node][1]+=min(dp[i][0],dp[i][1])

dfs(1)
print(min(dp[1][0],dp[1][1]))
