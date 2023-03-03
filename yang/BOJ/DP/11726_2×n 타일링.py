# 31388KB / 44ms
# 블로그 및 질문게시판 참고
dp = [0]*1001
dp[1], dp[2] = 1, 2
n = int(input())
ans = 0
for i in range(3, n+1):
   dp[i] = dp[i-1]+dp[i-2]
print(dp[n]%10007)