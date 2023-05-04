# 이분그래프 찾아봄
# 52520KB / 1228ms
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dq = deque()
    dq.append(start)
    color_visited[start] = 0
    while dq:
        s = dq.popleft()
        for i in graph[s]:
            if color_visited[i] == color_visited[s]:
                return False
            elif color_visited[i] == -1:
                color_visited[i] = 1 if color_visited[s]==0 else 0
                dq.append(i)
    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    color_visited = [-1]*(V+1) # -1이면 방문안함, 0이면 빨강, 1이면 파랑
    for i in range(1, V+1):
        if color_visited[i]==-1:
            if not bfs(i):
                print("NO")
                break
    else: print("YES")