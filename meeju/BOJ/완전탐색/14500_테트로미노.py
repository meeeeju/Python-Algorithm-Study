# 블로그 참조
import sys
input = sys.stdin.readline

'''
5 5 세로 N 가로 M 
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1'''

N, M = map(int, input().split())
board = []
visited = [[False] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    board.append(list(map(int, input().split())))

answer = 0

def dfs(x, y, mysum, depth):
    global answer

    if depth == 3:
        answer = max(answer, mysum)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                continue

            if depth == 1:  # ㅗ 모양은 DFS로 만들 수 없으므로 예외처리
                visited[nx][ny] = True
                dfs(x, y, mysum + board[nx][ny], depth + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, mysum + board[nx][ny], depth + 1)
            visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False

print(answer)