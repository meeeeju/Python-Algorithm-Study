# 	72584	992
import sys
input = sys.stdin.readline

'''
4 4
9 14 29 7
1 31 6 13
21 26 40 16
8 38 11 23
3
1 1 3 2
1 1 1 4
1 1 4 4'''

N,M = map(int,input().split()) # N : 세로, M : 가로

dp = [0 for _ in range(N+1)]
dp[0]=[0 for _ in range(M+1)]
for i in range(N):
    temp =list(map(int,input().split()))
    dp[i+1]=[0]+temp
for i in range(1,N+1): # 누적합 구하기
    for j in range(1,M+1):
        dp[i][j]+=dp[i][j-1]+dp[i-1][j]
        dp[i][j]-= dp[i-1][j-1]

K = int(input())
for _ in range(K):
    x1,y1,x2,y2= map(int,input().split())
    x1-=1
    y1-=1 
    ans = dp[x2][y2]+dp[x1][y1]-(dp[x1][y2]+dp[x2][y1])
    print(ans)
    

