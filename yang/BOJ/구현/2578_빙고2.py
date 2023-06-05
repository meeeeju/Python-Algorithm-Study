# 31256KB / 40ms
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
                row[i] += 1
                col[j] += 1
                return i, j

def checkLeftUpDiagonal():
    if not visited[2][2]: return False
    x, y = 0, 0
    while 0<=x<5 and 0<=y<5:
        if not visited[x][y]: return False
        x, y = x+1, y+1
    return True
def checkRightUpDiagonal():
    if not visited[2][2]: return False
    x, y = 0, 4
    while 0<=x<5 and 0<=y<5:
        if not visited[x][y]: return False
        x, y = x+1, y-1
    return True

bingo = 0
visited = [[False]*5 for _ in range(5)]
row = [0]*5
col = [0]*5
rdiagonal, ldiagonal = False, False
for i in range(5):
    for j in range(5):
        x, y = find(request[i][j])
        if row[x] == 5:
            bingo += 1
        if col[y] == 5:
            bingo += 1
        if i >=1 :
            if not ldiagonal:
                ldiagonal = checkLeftUpDiagonal()
                if ldiagonal: bingo += 1
            if not rdiagonal:
                rdiagonal = checkRightUpDiagonal()
                if rdiagonal: bingo += 1
        if bingo >= 3:
            print(i*5+(j+1))
            break
    if bingo >= 3: break