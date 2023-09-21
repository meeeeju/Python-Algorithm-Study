# 블로그 참고 
import sys
input = sys.stdin.readline


'''
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80'''

T = int(input())



for _ in range(T):

    n = int(input())
    stickers = [0 for _ in range(2)]

    for i in range(2):
        line =  list(map(int,input().split()))
        stickers[i]=line

    dp = [0,0]
    for i in range(2):
        dp[i] = [0] + stickers[i]

    for i in range(2,n+1):
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])

    print(max(dp[0][n],dp[1][n]))

