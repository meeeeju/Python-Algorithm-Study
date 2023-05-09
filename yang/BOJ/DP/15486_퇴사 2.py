# 168868KB / 2756ms

import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)
dp = [0]*(n+1)
# dp[i] : i번째 날에 상담을 했을 때 얻을 수 있는 최대 수익
a = 0
for i in range(n):
    if i+t[i] <= n:
        dp[i+t[i]] = max(a+p[i], dp[i+t[i]], dp[i]+p[i])
        # dp[i+t[i]] = max(i 이전날에서 상담, 이전값, i에서 상담)
    a = max(dp[i], a) # => i 이전에 값들 중 가장 큰 값
    
print(max(dp))