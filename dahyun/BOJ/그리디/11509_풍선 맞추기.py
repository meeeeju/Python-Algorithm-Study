# 218280 KB / 5904 ms (pypy)
import sys
input = sys.stdin.readline
N=int(input())
nlist = list(map(int,input().split()))
need=0
while True:
    h=max(nlist)
    if h==0:
        print(need)
        break
    for i in range(N):
        if nlist[i]==h: 
            h-=1
            nlist[i]=0
    need+=1
