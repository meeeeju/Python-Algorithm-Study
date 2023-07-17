# 31256 KB / 40 ms
import sys
input = sys.stdin.readline
dp=[0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(90)]  # 최대 100 까지
for i in range(11,101): dp[i]=dp[i-1]+dp[i-5]
for _ in range(int(input())):
    print(dp[int(input())])
