# 31268KB / 48ms
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())
war = []
visited = [[False]*N for _ in range(M)]
for _ in range(M):
    war.append(input().strip())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, state, count):
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0<=cx<M and 0<=cy<N and war[cx][cy]==state and not visited[cx][cy]:
            visited[cx][cy] = True
            count = dfs(cx, cy, state, count+1)
    return count

w, b = 0, 0
for k in range(M):
    for j in range(N):
        if not visited[k][j]:
            visited[k][j] = True
            c = dfs(k, j, war[k][j], 1)
            if war[k][j] == 'W':
                w += c**2
            else:
                b += c**2
print(w, b)