# 블로그 참고 근데 약간 잘 모르겠음..
# 315220KB / 5836ms
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0 # 본인이 얼리가 아니면 얼리 개수 0
    dp[node][1] = 1 # 본인이 얼리면 얼리 개수 1 (색칠할 때 1만큼 듦)
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0] += dp[i][1] # 현재 노드가 얼리가 아니라면 주변 노드는 얼리여야 함
            dp[node][1] += min(dp[i][0], dp[i][1]) # 현재 노드가 얼리면 주변 노드는 얼리이든 아니든 상관없음.

n = int(input())
graph = [[] for _ in range(n+1)]
for i in sys.stdin:
    try:
        u, v = map(int, i.split())
        graph[u].append(v)
        graph[v].append(u)
    except:
        break
visited = [False] * (n+1)
dp = [[0, 0] for _ in range(n+1)]
# dp[i][0] : i가 얼리어답터가 아닐때 최소 얼리어답터 개수 (모든 친구가 얼리어답터여야 함)
# dp[i][1] : i가 얼리어답터일때 최소 얼리어답터 개수 (주변 친구가 얼리어답터이거나 아니어도 됨)
dfs(1)
print(min(dp[1][0], dp[1][1]))
