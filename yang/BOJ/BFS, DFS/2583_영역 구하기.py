# 31256KB / 52ms
import sys
input = sys.stdin.readline

def dfs(i, j):
    # 저번에 아파트 단지 bfs로 풀었으니 이번엔 dfs로 풀어봤음
    area = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack = [(i, j)]
    paper[i][j] = True
    while stack:
        x, y = stack.pop()
        area += 1
        for v in range(4):
            nextX = x+dx[v]
            nextY = y+dy[v]
            if 0<=nextX<N and 0<=nextY<M and not paper[nextX][nextY]:
                stack.append((nextX, nextY))
                paper[nextX][nextY] = True
    return area

M, N, K = map(int, input().split())
paper = [[False]*M for _ in range(N)] # 왼쪽 아래가 0인건 구현안해도 문제푸는데 상관없음
for _ in range(K):
    startN, startM, endN, endM = map(int, input().split())
    for i in range(startN, endN):
        for j in range(startM, endM):
            paper[i][j] = True # endN-1, endM-1 까지 돌게됨 => 직사각형!!


area = []
for i in range(N):
    for j in range(M):
        if not paper[i][j]:
            area.append(dfs(i, j))
area.sort()
print(len(area))
print(*area)
