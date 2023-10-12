# 34096KB / 68ms
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
L = int(input())

changeList = []
for _ in range(L):
    x, c = input().split()
    changeList.append((int(x), c))
changeList.sort()

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

d = 0
dq = deque()
dq.append((0, 0))
headX = 0
headY = 0
time = 0
while True:
    time += 1
    headX += dx[d]
    headY += dy[d]

    if headX < 0 or headX >= N or headY < 0 or headY >= N:
        break
    if (headX, headY) in dq:
        break

    if board[headX][headY] == 1:
        board[headX][headY] = 0
        dq.append((headX, headY))
    else:
        dq.append((headX, headY))
        tx, ty = dq.popleft()

    if len(changeList) > 0 and time == changeList[0][0]:
        if changeList[0][1] == "L":
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4
        changeList.pop(0)

print(time)