# 블로그 참고
import sys

'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200'''

from sys import stdin

n = int(stdin.readline())
t, p = [], []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    ti, pi = map(int, stdin.readline().split())
    t.append(ti)
    p.append(pi)

k = 0
for i in range(n):
    k = max(k, dp[i])
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(k + p[i], dp[i + t[i]])

print(max(dp))


