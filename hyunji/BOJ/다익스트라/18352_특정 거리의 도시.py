#메모리 :101160 시간 :1824ms
import sys
input=sys.stdin.readline
from collections import deque

N,M,K,X=map(int,input().split())
liist=[[] for i in range(N+1)]
visited=[False]*(N+1)
distance=[0]*(N+1)

for i in range(M):
    A,B=map(int,input().split())
    liist[A].append(B)

def bfs(start):
    liist2=[]
    queue=deque([start])
    visited[start]=True
    distance[start]=0
    
    while queue:
        now=queue.popleft()
        for i in liist[now]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
                distance[i]=distance[now]+1
                if distance[i]==K:
                    liist2.append(i)
    if len(liist2)==0:
        print(-1)
    else:
        liist2.sort()
        for i in liist2:
            print(i,end='\n')
bfs(X)
