# 36132 KB/	192 ms
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
train=['00000000000000000000' for _ in range(N+1)] # 기차 칸 수는 20개
result=set() # 결과를 나타낼 set
for _ in range(M):
    nlist=list(map(int,input().split()))
    if len(nlist)>2: # 입력 받은 수가 3개
        if nlist[0]==1: train[nlist[1]]=train[nlist[1]][:nlist[2]-1]+'1'+train[nlist[1]][nlist[2]:] # 1번일 때, 그 자리에 손님 앉히기
        else: train[nlist[1]]=train[nlist[1]][:nlist[2]-1]+'0'+train[nlist[1]][nlist[2]:] # 2번일 때, 그 자리에 손님 빼기
    else:
        if nlist[0]==3: train[nlist[1]]='0'+train[nlist[1]][:19] # 오른쪽으로 밀기
        else: train[nlist[1]]=train[nlist[1]][1:20]+'0' # 왼쪽으로 밀기
for i in range(1,N+1): result.add(train[i])  # 겹치는 것 다 삭제됨
print(len(result))
