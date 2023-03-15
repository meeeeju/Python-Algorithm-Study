# 31256 KB / 40 ms
import sys
input=sys.stdin.readline
N=int(input())
A,B = map(int,input().split()) # A : 도우가격(전체 가격) B : 토핑가격
C=int(input()) # C : 도우 열량
nlist=[int(input()) for _ in range(N)]
nlist.sort(reverse=True) # 토핑 내림차순 정렬
for i in range(N):
   if C//A<=(C+nlist[i])//(A+B) :  # 열량 / 가격 값이 더 작은 것으로 초기화
       A+=B
       C+=nlist[i]
print(C//A)

