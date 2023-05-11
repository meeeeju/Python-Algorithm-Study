# 블로그 참고 - 5548 ms
import sys
input=sys.stdin.readline
def dfs(start):
    visited[start]=True
    if not graph[start]:
        dp[start][0]=0  # start일 때 얼리어답터 아닐 때
        dp[start][1]=1  # start일 때 얼리어답터
    else:   
        for g in graph[start]:
            if not visited[g]:
                dfs(g)
                dp[start][1]+=min(dp[g][0],dp[g][1]) # start일 때 얼리어답터
                dp[start][0]+=dp[g][1]  # start일 때 얼리어답터 아닐 때
        dp[start][1]+=1
N= int(input())
graph=[[] for _ in range(N+1)]
dp=[[0,0] for _ in range(N+1)]  # [현재 노드][얼리어 답터 여부]
visited=[False for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(1)
print(min(dp[1][0],dp[1][1]))

'''
서브 트리의 최적해를 구하는 것이므로 , 내 자식 노드들은 이미 최적해를 구해 왔다고 생각
'''
