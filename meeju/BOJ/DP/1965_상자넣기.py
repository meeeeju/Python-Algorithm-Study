# 31256kb  / 228ms
import sys
input = sys.stdin.readline

'''
8
1 6 2 5 7 3 5 6'''

n = int(input())    # 상자의 갯수
box_list = list(map(int,input().split()))

dp = [1 for _ in range(n)]  # 1 로 초기화  (자신의 상자)


for i in range(1,n):
    for j in range(i):
        if box_list[i] > box_list[j]:   # 나의 상자(i)가 나보다 앞에 있는 상자(j) 보다 크다면
            dp[i]= max(dp[j]+1,dp[i])

print(max(dp))

