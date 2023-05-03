# 41132KB / 812ms
from collections import deque
# 가장 높은 층, 현재 층, 목표층
F, S, G, up, down = map(int, input().split())
visited = [False]*(F+1) # 1층 ~ F층
dq = deque()
dq.append((0, S))
visited[S] = True
while dq:
    distance, now = dq.popleft()
    if now == G:
        print(distance)
        break
    if now+up <= F and not visited[now+up]:
        dq.append((distance+1, now+up))
        visited[now+up] = True
    if now-down >= 1 and not visited[now-down]:
        dq.append((distance+1, now-down))
        visited[now-down] = True
else:
    print("use the stairs")