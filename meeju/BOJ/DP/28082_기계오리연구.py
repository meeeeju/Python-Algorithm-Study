import sys
input = sys.stdin.readline


'''
3 2
1 100 10'''

N,K = map(int,input().split())
electronics = list(map(int,input().split()))
all_sum = 50000
dp= [float('inf') for _ in range(all_sum+1)]
dp[0]=0


# dp[k] : 전력량 k 일때 나올 수 최소 배터리 갯수
#500*50000 = 25000000


for i in range(N):
    
    for j in range(all_sum-electronics[i],-1,-1):
        dp[j+electronics[i]]= min(dp[j+electronics[i]],dp[j]+1)
    # for j in range(0,all_sum-electronics[i]+1):
    #     dp[j+electronics[i]]= min(dp[j+electronics[i]],dp[j]+1)

cnt = 0
result = []
for i in range(1,all_sum+1):
    if dp[i] <=K:
        result.append(i)
        cnt +=1
print(cnt)
print(*result)

