# 31256KB / 164ms
import sys
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(input().rstrip())) # 'CPP' -> ['C', 'P', 'P']

def checkMax(ni, nj):
    result = 1
    count = 1
    for k in range(1, N):
        if board[ni][k-1] == board[ni][k]:
            count += 1
            result = max(result, count)
        else :
            count = 1

    count = 1
    for k in range(1, N):
        if board[k-1][nj] == board[k][nj]:
            count += 1
            result = max(result, count)
        else :
            count = 1
    return result


di = [0, 1]
dj = [1, 0]
d = [(0, 1), (1, 0)]
ans = 1
for i in range(N):
    for j in range(N):
        ans = max(ans, checkMax(i, j))
        for v in d: # 우, 하
            ni = v[0]+i
            nj = v[1]+j
            if 0<=ni<N and 0<=nj<N and board[ni][nj] != board[i][j]:
                # 교체
                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
                # 최대값 체크
                ans = max(ans, checkMax(ni, nj), checkMax(i, j))
                # 교체
                board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
print(ans)