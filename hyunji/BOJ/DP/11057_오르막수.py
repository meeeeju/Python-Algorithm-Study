#메모리 :31256 시간 :44
import sys
input=sys.stdin.readline

n=int(input())
dp=[[1]*10 for _ in range(n)]
summ=0

for i in range(n-1):
    for j in range(1,10):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
dp.sort(key=lambda x:x[1])

for i in range(0,10):
    summ+=dp[n-1][i]
print(summ%10007)
