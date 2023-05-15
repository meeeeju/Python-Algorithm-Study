# 35500 KB / 120 ms
import sys
input = sys.stdin.readline
N=int(input())
nlist = [int(input()) for _ in range(N)]
nlist.sort()   # nlist 정렬
result=0
for i in range(N):  
    result=max(result,nlist[i]*(N-i)) # 현재 중량값 * 해당 값으로 버틸 수 있는 로프 수
print(result)
