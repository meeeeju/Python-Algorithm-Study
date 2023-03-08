# 39032 KB / 196 ms
import sys

N=int(sys.stdin.readline())
matrix=[[0 for _ in range(N+1)] for _ in range(N+1)]
A=[-1]+list(map(int,sys.stdin.readline().split()))
dp=[1 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if A[i]>A[j]: dp[j]=max(dp[i]+1,dp[j]) # dp[i]의 다음 수열이 큰지, dp[j] 기존 값이 더 큰지
print(max(dp))
