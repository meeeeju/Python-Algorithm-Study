# 35564KB / 7884ms
# 블로그 참고
from collections import deque
N, K = map(int, input().split())
q = deque()
q.append((K, 0, str(K)))
visited = [False]*200001
while q:
    num, time, move = q.popleft()
    if num == N:
        print(time)
        print(move)
        break
    if num%2==0 and not visited[num//2]:
        q.append((num//2, time+1, f"{num//2} {move}"))
        visited[num//2] = True
    if num+1<=200000 and not visited[num+1]:
        q.append((num+1, time+1, f"{num+1} {move}"))
        visited[num+1] = True
    if num-1>=0 and not visited[num-1]:
        q.append((num-1, time+1, f"{num-1} {move}"))
        visited[num-1] = True