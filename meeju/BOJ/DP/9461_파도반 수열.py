# 31256	40
import sys
input = sys.stdin.readline


input_n = []
dp=[]
for i in range(int(input())):
    input_n.append(int(input()))

max_n = max(input_n)
dp =[1 for _ in range(max_n+1)]
dp[4]=2
dp[5]=2


def p(n):
    for i in range(6,n+1):
        dp[i]=dp[i-1]+dp[i-5]

p(max_n)

for k in input_n:
    print(dp[k])