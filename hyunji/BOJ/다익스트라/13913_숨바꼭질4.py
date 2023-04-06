#블로그참고
#메모리 :38456 시간 :116ms
from collections import deque
count=0
liist=[]

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001

if N>K:
    count=N-K
    for i in range(count+1):
        liist.append(N)
        N=N-1
    print(count)
    print(*liist)
        
else:
    bfs()
