# 31256 KB / 40 ms
import sys
input = sys.stdin.readline
dp=[1,2,4]
for i in range(3,11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])
for _ in range(int(input())):
    n = int(input())
    print(dp[n-1])
    
    
