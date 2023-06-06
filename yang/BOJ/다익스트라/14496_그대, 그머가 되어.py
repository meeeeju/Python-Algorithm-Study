# 34144KB / 72ms
# 질문게시판 참고

import sys
from collections import deque
input = sys.stdin.readline

start, goal = map(int, input().split())
N, M = map(int, input().split())
pairs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    pairs[a].append(b)
    pairs[b].append(a)

go = deque()
visited = [False]*(N+1)
go.append((start, 0))
visited[start] = True
while go:
    char, count = go.popleft()
    if char == goal:
        print(count)
        break
    for i in pairs[char]:
        if not visited[i]:
            visited[i] = True
            go.append((i, count+1))
else:
    print(-1)