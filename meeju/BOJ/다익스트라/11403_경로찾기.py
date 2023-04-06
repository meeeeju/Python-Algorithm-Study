# 	31256kb /	56ms
import sys
input = sys.stdin.readline

N= int(input())

adj_list = [ [] for _ in range(N)]
graph = [ [] for _ in range(N)]
result = [ [0]*N for _ in range(N)]

def dfs(s):

    def recur(v):
        visited[v]=True
        for w in graph[v]:
            if w == s :
                result[s][w] = 1
                # print("cycle occurs")
            if not visited[w]:  # 방문하지 않은 정점
                result[s][w]=1
                recur(w)

    visited= [ False for _ in range(N)]
    recur(s)


for i in range(N):
    adj_list[i]=list(map(int,input().split()))

if N == 1:
    print(0)
else:
    for i in range(N):
        for w in range(N):
            if adj_list[i][w]==1:
                graph[i].append(w)

    for i  in range(N):
        dfs(i)

    for i  in range(N):
        print(*result[i])