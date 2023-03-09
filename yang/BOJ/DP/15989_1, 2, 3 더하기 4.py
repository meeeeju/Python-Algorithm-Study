# 31256KB / 48ms
# 블로그 참고... dp 너무 어려워요....
# https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-15989-%ED%95%B4%EC%84%A4-python-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-4
import sys
input = sys.stdin.readline
dp = [1]*(10001) # 다 1로 나타낼 수는 있기 때문에 1로 dp 초기화

for i in range(2,10001):
    dp[i] += dp[i - 2] # i-2값에서 2가 더 들어올 때
    
for i in range(3,10001):
    dp[i] += dp[i - 3] # i-3값에서 3이 더 들어올 때

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])