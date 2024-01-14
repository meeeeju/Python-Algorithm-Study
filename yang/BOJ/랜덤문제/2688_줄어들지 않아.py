# 31120KB / 40ms

import sys
input = sys.stdin.readline

# dp[i][j] : j로 끝나는 i자리 수
dp = [[-1]*10 for _ in range(65)]

dp[0] = [0]*10
dp[1] = [1]*10 # dp[1] 은 한자리수 => 0~9

for i in range(2, 65):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n]))