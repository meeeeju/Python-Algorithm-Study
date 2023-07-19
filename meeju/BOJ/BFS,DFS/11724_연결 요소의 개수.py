# 65172	712
# dfs stack 으로 풀면 시간초과뜸 왜 >>..?

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


'''
6 5
1 2
2 5
5 1
3 4
4 6

1'''



N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt = 0

for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(s):
    def recur(v):
        visited[v]= True
        for w in graph[v]:
            if not visited[w]:
                recur(w)
    recur(s)


def dfs_stack(s):
    
    stack = []
    stack.append(s)

    while stack :
        
        v = stack.pop()
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                stack.append(w) 

for i in range(1,N+1):
    if not visited[i]:
        dfs_stack(i)
        cnt += 1

print(cnt)