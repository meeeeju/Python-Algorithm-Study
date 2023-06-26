# 35692 KB / 100 ms
import sys
input = sys.stdin.readline
from itertools import permutations  
def check(llist):  # 가장 큰 차이 구하기
    global result
    total=0
    for i in range(1,N):
        total+=abs(llist[i-1]-llist[i])
    result=max(result,total)
N= int(input())
nlist = list(map(int,input().split()))
perm = list(permutations(nlist, N))  # 조합 사용
result=0
for llist in perm:
    check(llist)
print(result)
