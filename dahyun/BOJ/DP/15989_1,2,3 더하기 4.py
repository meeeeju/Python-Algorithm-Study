# 31256 KB / 44 ms
import sys
dp=[0]*10001
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=3
odd_count=2
for i in range(4,10001):
    dp[i]=dp[i-1]+dp[i-2]-dp[i-3]
    if i%3 ==0 : dp[i]+=1  
    
for _ in range(int(sys.stdin.readline())):
    print(dp[int(sys.stdin.readline())])
