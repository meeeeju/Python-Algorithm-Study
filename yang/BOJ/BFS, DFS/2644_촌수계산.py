# 34184KB / 64ms
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
red, blue = map(int, input().split())
m = int(input())
parent = [i for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split()) # y의 부모가 x
    parent[y] = x

red_visited = [-1]*(n+1)
blue_visited = [-1]*(n+1)
dq = deque()
dq.append((0, red, 'r')) # (거리, 사람번호, 출발지)
dq.append((0, blue, 'b')) # multi BFS

while dq:
    distance, node, start = dq.popleft()
    if start == 'r':
        if blue_visited[node] >= 0:
            print(distance + blue_visited[node])
            break
        if red_visited[node] < 0:
            red_visited[node] = distance
            dq.append((distance+1, parent[node], start))
    else:
        if red_visited[node] >= 0:
            print(distance + red_visited[node])
            break
        if blue_visited[node] < 0:
            blue_visited[node] = distance
            dq.append((distance+1, parent[node], start))
else:
    print(-1)