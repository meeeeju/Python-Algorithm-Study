# 31256 KB / 220 ms
import sys
input=sys.stdin.readline
N=int(input())
nlist = list(map(int,input().split()))
dp=[1 for _ in range(N+1)]
for i in range(N):
    for j in range(i,N):
        if nlist[i]<nlist[j]: dp[j] = max(dp[j],dp[i]+1) # 시작점 + 1, 전 단계 값
print(max(dp))
