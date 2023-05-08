# 31256KB / 184ms
import sys
input = sys.stdin.readline

n = int(input())
blocks = input().strip()
MAX_INT = 10000001
next_block = {'B':'O', 'O':'J', 'J':'B'}
dp = [MAX_INT]*n # dp[i] : i까지 왔을 때, 필요한 에너지양
dp[0] = 0
for i in range(n):
    for j in range(i+1, n):
        if blocks[j] == next_block[blocks[i]]:
            dp[j] = min(dp[j], dp[i]+(j-i)**2)
if dp[n-1] == MAX_INT:
    print(-1)
else:
    print(dp[n-1])
