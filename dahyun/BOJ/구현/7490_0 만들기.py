# bfs : 31256 KB / 144 ms
# dfs : 31256 KB / 140 ms
# 여러번 돌려봤을 때 비슷함 ! 
# 계속 출력 형식이 잘못되었다고 떠서 선아 코드에서 출력 부분 확인함
import sys
def bfs():
    queue=[(1,'1')]
    while queue:
        n,tlist = queue.pop(0)
        for i in range(3):
            if n==N-1:
                if eval((tlist+Calculate[i]+str(N)).replace(' ',''))==0:
                    print(tlist+Calculate[i]+str(N))
            else: queue.append((n+1,tlist+Calculate[i]+str(n+1)))
            
def dfs(n,tlist):
    for i in range(3):
        if n==N-1:
            if eval((tlist+Calculate[i]+str(N)).replace(' ',''))==0:
                print(tlist+Calculate[i]+str(N))
        else: dfs(n+1,tlist+Calculate[i]+str(n+1))
Calculate=[' ','+','-']
for _ in range(int(sys.stdin.readline())):
    N=int(sys.stdin.readline())
    bfs()
    # dfs(1,'1')
    print()
    
