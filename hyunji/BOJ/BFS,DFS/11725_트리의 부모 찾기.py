#메모리 :63012 시간:4392ms
import sys
sys.setrecursionlimit(1000000)
N=int(input())
array=[[] for i in range(N+1)]
visit=[0]*(N+1)

for i in range(N-1):
    a,b=map(int,input().split())
    array[a]+=[b]
    array[b]+=[a]
   
def dfs(n):
    for ab in array[n]:
        if visit[ab]==0:
            visit[ab]=n
            dfs(ab)
           
dfs(1)
for i in range(2,N+1):
    print(visit[i])
