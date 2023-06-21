
# 129564	2712
# 블로그 참고
# 깊은 복사 : https://crackerjacks.tistory.com/14 (쉽게 설명 잘 해놓음)

from collections import deque
import copy
import sys
input = sys.stdin.readline

'''
7 7  #  N : 세로, M : 가로
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''

d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque()
    
    test_map = copy.deepcopy(lab_map)
    for i in range(N):  # 우선 queue에 2인거 다 넣어주기
        for j in range(M):
            if test_map[i][j] == 2:
                queue.append((i,j))

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            dy = y+d[i][0]
            dx = x+d[i][1]

            if (0 <= dy < N) and (0 <= dx < M):
                if test_map[dy][dx] == 0:
                    test_map[dy][dx] =2
                    queue.append((dy,dx))

    global result
    count = 0
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 0:
                count +=1         
    result = max(result, count)

    return


def make_wall(count):   # 벽 만들어주는 함수
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 0:  # 빈 경우
                lab_map[i][j] = 1
                make_wall(count+1)
                lab_map[i][j] = 0   # 다시 초기화(0으로 바꿔주기)


N,M = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(N)]

result = 0
make_wall(0)

print(result)