# 31256	772
# 블로그 참고 (https://week-year.tistory.com/172)
# dp 로 풀어야되는지 몰랐음

dp = [0 for _ in range(5001)] # L (1 ≤ L ≤ 5000) 
dp[0] = 1   # 아무것도 안 세어지는 경우도 1개이기 때문

for n in range(2, 5001, 2): # 짝수만 가능하므로
    for i in range(2, n + 1, 2):
        dp[n] += dp[i - 2] * dp[n - i]
    dp[n] %= 1000000007

for _ in range(int(input())):
    print(dp[int(input())])
