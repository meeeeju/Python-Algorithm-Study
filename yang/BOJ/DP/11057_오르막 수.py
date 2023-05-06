# 31256KB / 48ms
n = int(input())
MOD = 10007
dp = [[0]*(10) for _ in range(1001)] # dp[i][j] : j로 시작하는 i자리 오르막 수
for j in range(10):
    dp[1][j] = 1
    dp[2][j] = 10-j
for i in range(3, n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:]) % MOD
print(sum(dp[n]) % MOD)