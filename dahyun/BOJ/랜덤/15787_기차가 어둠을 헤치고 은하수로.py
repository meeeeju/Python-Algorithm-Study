#BaekJoon 15787 기차가 어둠을 헤치고 은하수로
# 36132 KB/	192 ms
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
train=['00000000000000000000' for _ in range(N+1)]
result=set()
for _ in range(M):
    nlist=list(map(int,input().split()))
    if len(nlist)>2: 
        if nlist[0]==1: train[nlist[1]]=train[nlist[1]][:nlist[2]-1]+'1'+train[nlist[1]][nlist[2]:]
        else: train[nlist[1]]=train[nlist[1]][:nlist[2]-1]+'0'+train[nlist[1]][nlist[2]:]
    else:
        if nlist[0]==3: train[nlist[1]]='0'+train[nlist[1]][:19] # 오른쪽
        else: train[nlist[1]]=train[nlist[1]][1:20]+'0' # 왼쪽
for i in range(1,N+1): result.add(train[i])
print(len(result))
