#블로그 참고 
# 31256 KB / 192 ms
import sys
input=sys.stdin.readline
N=int(input())
nlist=list(map(str,input().strip()))
dp=[999999999 for _ in range(N)]
dp[0]=0
for i in range(1,N):
    for j in range(i): # 그 자리를 기준의 최솟값을 앞에서부터 확
        if (nlist[i]=='O' and nlist[j]=='B') or (nlist[i]=='J' and nlist[j]=='O') or (nlist[i]=='B' and nlist[j]=='J'):
            dp[i]=min(dp[i],dp[j]+pow(i-j,2))
print(dp[N - 1] if dp[N - 1] != 999999999 else -1)
