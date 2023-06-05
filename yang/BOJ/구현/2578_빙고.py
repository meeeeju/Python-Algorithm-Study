# 31256KB / 44ms
import sys
input = sys.stdin.readline
board = []
request = []
for _ in range(5):
    board.append(tuple(map(int, input().split())))
for _ in range(5):
    request.append(tuple(map(int, input().split())))

def find(r):
    # 보드판에서 어디있는지 찾기
    for i in range(5):
        for j in range(5):
            if board[i][j] == r:
                visited[i][j] = True
                return i, j

def check(r):
    i, j = find(r)
    # visited 했을 때, 몇개의 빙고가 만들어지는지 찾기
    horizontal = 1 # 가로
    vertical = 1 # 세로
    leftUpDiagonal = 1 # 좌상향 대각선
    rightUpDiagonal = 1 # 우상향 대각선
    # 가로
    x, y = i, j-1
    while 0<=y<5:
        if not visited[x][y]: break
        y -= 1
        horizontal += 1
    x, y = i, j+1
    while 0<=y<5:
        if not visited[x][y]: break
        y += 1
        horizontal += 1
    # 세로
    x, y = i-1, j
    while 0<=x<5:
        if not visited[x][y]: break
        x -= 1
        vertical += 1
    x, y = i+1, j
    while 0<=x<5:
        if not visited[x][y]: break
        x += 1
        vertical += 1
    # 좌상향
    x, y = i-1, j-1
    while 0<=x<5 and 0<=y<5:
        if not visited[x][y]: break
        x, y = x-1, y-1
        leftUpDiagonal += 1
    x, y = i+1, j+1
    while 0<=x<5 and 0<=y<5:
        if not visited[x][y]: break
        x, y = x+1, y+1
        leftUpDiagonal += 1
    # 우상향
    x, y = i+1, j-1
    while 0<=x<5 and 0<=y<5:
        if not visited[x][y]: break
        x, y = x+1, y-1
        rightUpDiagonal += 1
    x, y = i-1, j+1
    while 0<=x<5 and 0<=y<5:
        if not visited[x][y]: break
        x, y = x-1, y+1
        rightUpDiagonal += 1
    for k in [horizontal, vertical, leftUpDiagonal, rightUpDiagonal]:
        if k >= 5:
            global bingo
            bingo += 1

bingo = 0
visited = [[False]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        check(request[i][j])
        # print(bingo)
        if bingo >= 3:
            print(i*5+(j+1))
            break
    if bingo >= 3: break
# print(visited)