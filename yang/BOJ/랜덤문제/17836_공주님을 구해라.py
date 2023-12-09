# 33320KB / 64ms
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, T = map(int, input().split())
castle = []
for _ in range(N):
    castle.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False]*M for _ in range(N)]
pq = [(0, 0, 0)] # 용사 출발 (시간, x, y)
visited[0][0] = True
ans = "Fail"
while pq:
    t, x, y = heappop(pq)
    if t > T:
        break
    if x == N-1 and y == M-1:
        ans = t
        break
    for v in range(4):
        nextX = x + dx[v]
        nextY = y + dy[v]
        if 0 <= nextX < N and 0 <= nextY < M and not visited[nextX][nextY]:
            visited[nextX][nextY] = True
            if castle[nextX][nextY] == 0 :
                heappush(pq, (t + 1, nextX, nextY))
            elif castle[nextX][nextY] == 2:
                nextT = t + 1 + (N - 1 - nextX) + (M - 1 - nextY)
                heappush(pq, (nextT, N-1, M-1))
print(ans)