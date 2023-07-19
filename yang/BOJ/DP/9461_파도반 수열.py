# 31256KB / 60ms
# 블로그 참고
# https://yabmoons.tistory.com/518
t = int(input())
dp = [0, 1, 1, 1, 2, 2] + [0]*96
for _ in range(t):
    n = int(input())
    for i in range(5, n+1):
        if dp[i] != 0: continue
        dp[i] = dp[i-1]+dp[i-5]
    print(dp[n])