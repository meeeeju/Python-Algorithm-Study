# 블로그 참고
# https://chldkato.tistory.com/114

import sys
input = sys.stdin.readline

# 1. 과정을 진행하면서 mem에 이미 저장된 값이 0이면 목적지까지 갈 수 없으므로 0을 반환한다
# 2. 1 이상의 값이면 이전에 그만큼 방문 경로가 있으므로 해당 값을 반환해서 더해준다
# 3. -1이면 방문하지 않은 경로이므로 dfs + dp 수행
def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if mem[x][y] != -1:
        return mem[x][y]
    mem[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if a[nx][ny] < a[x][y]:
                mem[x][y] += dfs(nx, ny)
    return mem[x][y]

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
mem = [[-1]*n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(dfs(0, 0))