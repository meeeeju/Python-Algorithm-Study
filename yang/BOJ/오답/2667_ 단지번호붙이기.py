# 31256KB / 48ms
import sys
input = sys.stdin.readline

def find(i, j):
    result = 1
    visited[i][j] = True
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        for v in range(4):
            nx = dx[v]+x
            ny = dy[v]+y
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False and apart[nx][ny]=='1':
                visited[nx][ny] = True
                stack.append((nx, ny))
                result += 1
    return result

N = int(input())
apart = []
ans = []
for _ in range(N):
    apart.append(input().rstrip())
visited = [[False]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(N):
        if visited[i][j]==False and apart[i][j]=='1':
            ans.append(find(i, j))

print(len(ans))
ans.sort()
print(*ans)