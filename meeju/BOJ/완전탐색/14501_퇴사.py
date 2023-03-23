# 31256kb /	44ms
# 블로그 참고 
import sys
input = sys.stdin.readline
'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200'''


N = int(input())

schedule = [0 for _ in range(N)]
dp =[ 0 for _ in range(N+1)]

for i in range(N):
    schedule[i]= tuple(map(int,input().split()))

for i in range(N):
    start = i+schedule[i][0]   # 상담 가능한 시작 일

    for j in range(start,N+1):
        if dp[j] < dp[i]+schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])

