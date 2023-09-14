# 34160KB / 1264ms (Python3)
# 134764KB / 340ms (PyPy3)

from sys import stdin
from collections import deque
input = stdin.readline

def bfs(l, night, goal):
    distance = [[-1]*l for _ in range(l)]
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [-2, 2, -2, 2, -1, 1, -1, 1]

    dq = deque()
    dq.append(night)
    distance[night[0]][night[1]] = 0
    while dq:
        x, y = dq.popleft()
        if x==goal[0] and y==goal[1]:
            break
        for v in range(8):
            next_x = dx[v] + x
            next_y = dy[v] + y
            if 0<=next_x<l and 0<=next_y<l and distance[next_x][next_y] == -1:
                distance[next_x][next_y] = distance[x][y]+1
                dq.append((next_x, next_y))
    return distance[goal[0]][goal[1]]

def solution():
    T = int(input())
    for _ in range(T):
        l = int(input())
        night = tuple(map(int, input().split()))
        goal = tuple(map(int, input().split()))
        # print("ans:", end = " ")
        print(bfs(l, night, goal))

if __name__=='__main__':
    solution()