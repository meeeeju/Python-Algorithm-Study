# 31256KB / 44ms
# 6개 이상 거르는 방법 질문게시판 참고
# https://www.acmicpc.net/problem/2615
# 6개 이상이면 정답이 아니게..
# 출력은 가장 왼쪽 바둑알..ㅠㅠ
# 조건 잘보기.. 어렵당

import sys
input = sys.stdin.readline

def check(color, i, j):
    if color == 1:
        save = check_board_black
    else:
        save = check_board_white
    for d in range(4):
        x = i+dx[d]
        y = j+dy[d]
        if 0<=x<19 and 0<=y<19:
            save[i][j][d] = save[x][y][d] + 1
        else:
            save[i][j][d] = 1
        if save[i][j][d] == 5:
            ans_candidate.append((color, i, j, d))



# 가로, 세로, 좌상향, 우상향
dx = [-1, 0, -1, -1]
dy = [0, -1, -1, 1]
ans = 0
ans_candidate = []
ans_width, ans_hegiht = 0, 0
check_board_black = [[[0, 0, 0, 0] for _ in range(19)] for _ in range(19)]
check_board_white = [[[0, 0, 0, 0] for _ in range(19)] for _ in range(19)]
for i in range(19):
    line = list(map(int, input().split()))
    for j in range(19):
        if line[j] == 1:
            check(1, i, j)
        if line[j] == 2:
            check(2, i, j)
            
while ans_candidate:
    color, i, j, d = ans_candidate.pop()
    if color == 1:
        save = check_board_black
    else:
        save = check_board_white
    x = i - dx[d]
    y = j - dy[d]
    if x<0 or y<0 or x>=19 or y>=19 or save[x][y][d] == 0:
        print(color)
        if d==3: #우상향 대각선일때
            print(i+1, j+1)
        else:
            print(i+4*dx[d]+1, j+4*dy[d]+1)
        break
else:
    print("0")