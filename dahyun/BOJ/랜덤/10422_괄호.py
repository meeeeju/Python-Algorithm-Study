# 질문게시판 - 카탈란 수 조합 , 블로그 참고
# https://week-year.tistory.com/172
import sys
input = sys.stdin.readline
dp = [0 for _ in range(5001)]
dp[0] = 1

for n in range(2, 5001, 2):
    for i in range(2, n + 1, 2):
        dp[n] += dp[i - 2] * dp[n - i]
    dp[n] %= 1000000007

for _ in range(int(input())):
    print(dp[int(input())])
