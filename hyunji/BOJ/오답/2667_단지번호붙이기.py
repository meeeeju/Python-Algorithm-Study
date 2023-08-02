import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
house = []
liist = []
visited = [[False] * (n) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    house.append(input().rstrip())
   

def bfs(i, j):
    visited[i][j] = True
    count = 0
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        count += 1

        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if 0 <= x < n and 0 <= y < n:
                if visited[x][y] == False and house[x][y] == "1":
                    visited[x][y] = True
                    queue.append((x, y))

    return count


for i in range(n):
    for j in range(n):
        if visited[i][j] == False and house[i][j] == "1":
            count = bfs(i, j)
            if count > 0:
                liist.append(count)

liist.sort()
print(len(liist))
print(*liist)
