# 31120	40
import sys
input = sys.stdin.readline

'''
3
2
3
4'''

T = int(input())
digit_list = []
for _ in range(T):
    digit_list.append(int(input()))
max_digit = max(digit_list)

dp = [[0 for _ in range(10)] for _ in range(max_digit+1)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(1,max_digit+1):
    dp[i][0] = 1

for i in range(2,max_digit+1):
    for j in range(1,10):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]

for i in digit_list:
    print(sum(dp[i]))
# for i in range(1,max_digit+1):
#     print(i,"번째",sum(dp[i]))
