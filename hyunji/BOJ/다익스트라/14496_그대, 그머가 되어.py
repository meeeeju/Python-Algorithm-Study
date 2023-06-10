#deque쓰는거 블로그참조
#메모리 :34160 시간 :72
import sys

input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)
queue = deque()
queue.append((a, 0))
visited[a] = True
while queue:
    curr, count = queue.popleft()
    if curr == b:
        print(count)
        break
    for i in graph[curr]:
        if visited[i] == False:
            visited[i] = True
            queue.append((i, count + 1))

else:
    print(-1)
