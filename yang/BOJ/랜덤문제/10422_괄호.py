# 블로그 참고
# https://velog.io/@junah201/%EB%B0%B1%EC%A4%80-10422-%EA%B4%84%ED%98%B8
# https://sapjilkingios.tistory.com/entry/SwiftDP-%EB%B0%B1%EC%A4%80-10422%EB%B2%88-%EA%B4%84%ED%98%B8
import sys
input = sys.stdin.readline

T = int(input())
dp = [0]*5001
dp[0] = 1 # 아무것도 넣지 않음 = 한가지 경우
for n in range(2, 5001, 2):
    for i in range(2, n+1, 2):
        dp[n] += dp[i-2]*dp[n-i]
        dp[n] %= 1000000007
for _ in range(T):
    l = int(input())
    print(dp[l])