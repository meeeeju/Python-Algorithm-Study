# 31256KB / 232ms
import sys
input = sys.stdin.readline

n = int(input())
boxs = list(map(int, input().split()))
dp = [1]*(n) # d[i] : i번째 상자까지 최대개수
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if boxs[i] < boxs[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))