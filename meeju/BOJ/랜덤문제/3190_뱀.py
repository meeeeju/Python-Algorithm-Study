# 왜 틀린지 모르겟움,,
import sys
from collections import deque
input = sys.stdin.readline
'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D'''

N = int(input()) # 정사각혀의 크기
K = int(input()) # 사과의 개수
board =[[0 for _ in range(N)] for _ in range(N)] # 보드

for i in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1

dir = int(input())   # 방향
dir_info = [] # 방향의 위치 담은 리스트
for i in range(dir):
    a,b= input().split()
    dir_info.append((int(a),b)) 
dir_info.reverse()


def move(): # time,next_t,next_dir, length

    time = 0
    snake_len = 1
    next_t ,next_dir =dir_info.pop()

    snake =deque([[0,0]])
    now_dir = 2 # 현재 방향 인덱스 번호 
    dir_option =[(0,-1),(-1,0),(0,1),(1,0)]

    while True:

        time = time+1   # 시간 증가시키기 
        if time == next_t : # 방향 변경해야하면, 변경시키기
            if next_dir =='D':
                now_dir = (now_dir+1)%4
            else:
                now_dir = (now_dir-1)%4
            if dir_info:
                next_t ,next_dir =dir_info.pop()

        x,y = snake[0]
        nx = x + dir_option[now_dir][0]
        ny = y + dir_option[now_dir][1]

        # 벽이랑 부딪히는지
        if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= N)  :
            return time
        # 자기 자신과 부딪히는지
        for i in range(len(snake)):
            if snake[i] == (nx,ny):
                return time

        # 사과있는 경우, 없는 경우 처리해주기 
        if board[nx][ny] :  # 사과가 있는 경우
            board[nx][ny] = 0
            snake_len +=1               # 몸 길이 증가하기
            snake.appendleft([nx,ny])     # 앞에 증가시키기
        else:
            snake.appendleft([nx,ny])
            snake.pop()                 # 줄여주기
            
print(move())

        
        



        

