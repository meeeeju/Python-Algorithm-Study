#블로그 참조
#메모리 :31256 시간:164ms
import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))

dp=[1 for _ in range(N)]
for i in range(1,N):
    for j in range(i):
        if A[i]<A[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
        
