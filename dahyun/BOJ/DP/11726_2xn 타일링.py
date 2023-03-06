#BackJoon 11726 2xn 타일링
#반례보다가 스포당함 ㅠ
# 31256 KB / 52 ms
import sys

n=int(sys.stdin.readline())
if n<3 : dp=[0]*4
else : dp=[0]*(n+1)

dp[0]=0
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
    

print(dp[n]%10007)
