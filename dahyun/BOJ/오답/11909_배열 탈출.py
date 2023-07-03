# 202512 KB / 1052 ms (pypy)
# 265212 KB / 7748 ms (python)
import sys
input = sys.stdin.readline
n = int(input())
nlist = [list(map(int,input().split())) for _ in range(n)]
dp = [[100000000 for _ in range(n)] for _ in range(n)]
dp[0][0]=0

for i in range(n):
    for j in range(n):
        temp1 = 10000000000000
        temp2 = 10000000000000
        if 0<i<n:
            if nlist[i-1][j]>nlist[i][j]: temp1 = dp[i-1][j]
            else: temp1 = dp[i-1][j]+(nlist[i][j]-nlist[i-1][j])+1
        if 0<j<n:
            if nlist[i][j-1]>nlist[i][j]: temp2 = dp[i][j-1]
            else: temp2 = dp[i][j-1]+(nlist[i][j]-nlist[i][j-1])+1
        dp[i][j]=min(dp[i][j],temp1,temp2)
print(dp[n-1][n-1])
