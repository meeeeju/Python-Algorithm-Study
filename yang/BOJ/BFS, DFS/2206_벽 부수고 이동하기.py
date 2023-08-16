# 블로그 & 질문게시판 보고 하긴 했는데 왜 벽을 부순것끼리는 visited를 같이 써도 되는지 모르겠음 가다가 막히면??
# https://www.acmicpc.net/board/view/27386
# 183460KB / 7036ms

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

map_list = []
for _ in range(N):
    map_list.append(input().rstrip())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# visited[x][y][벽 부쉈는지]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dq = deque()
dq.append((0, 0, 0)) # (x, y, is_break)
ans = -1
while dq:
    x, y, is_break = dq.popleft()
    if x==N-1 and y==M-1:
        ans = visited[x][y][is_break]
        break
    for v in range(4):
        next_x = x+dx[v]
        next_y = y+dy[v]
        if 0<=next_x<N and 0<=next_y<M:
            if is_break==0 and map_list[next_x][next_y] == "1":
                visited[next_x][next_y][1] = visited[x][y][0]+1
                dq.append((next_x, next_y, True))
            elif map_list[next_x][next_y]=="0" and visited[next_x][next_y][is_break]==0:
                visited[next_x][next_y][is_break] = visited[x][y][is_break]+1
                dq.append((next_x, next_y, is_break))
print(ans)





"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

map_list = []
for _ in range(N):
    map_list.append(input().rstrip())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

'''
x, y를 방문확인할때
x*M + y 번째가 1인지 0인지 보면 됨.

visited & (1 << x*M+y) == 0 : 방문안함

'''
visited = [[False]*M for _ in range(N)]

def visited_to_bit(visited)->int:
    result = 0
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j]:
                result |= (1 << M*i+j)
    return result

dq = deque()
dq.append((0, 0, 1, 0, True)) # (x, y, count, visited, can_break)
ans = -1
while dq:
    x, y, count, bit_visited, can_break = dq.popleft()
    if x==N-1 and y==M-1:
        ans = count
        break
    for v in range(4):
        next_x = x+dx[v]
        next_y = y+dy[v]
        if 0<=next_x<N and 0<=next_y<M:
            if can_break:
                if map_list[next_x][next_y]=="1":
                    dq.append((next_x, next_y, count+1, visited_to_bit(visited), False))
                elif not visited[next_x][next_y]:
                    dq.append((next_x, next_y, count+1, 0, True))
            else:
                if map_list[next_x][next_y]=="0" and bit_visited & (1 << next_x*M+next_y) == 0:
                    new_visited = bit_visited | (1 << next_x*M+next_y)
                    dq.append((next_x, next_y, count+1, new_visited, can_break))
print(ans)
"""