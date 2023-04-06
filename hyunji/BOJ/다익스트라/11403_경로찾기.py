#메모리 :34096 시간 :100ms
import sys
input=sys.stdin.readline
from collections import deque
N=int(input())
liist=[]

for i in range(N):
    liist.append(list(map(int,input().split())))

def dfs(n):
    for i in range(N):
        if visited[i]==0 and liist[n][i]==1:
            visited[i]=1
            dfs(i)
for i in range(N):
    visited=[0 for i in range(N)]
    dfs(i)
    print(*visited)
